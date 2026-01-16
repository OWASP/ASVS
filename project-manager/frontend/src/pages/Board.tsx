import { useParams, Link } from 'react-router-dom'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { boardApi, taskApi } from '../services/api'
import { DragDropContext, Droppable, Draggable, DropResult } from '@hello-pangea/dnd'
import { Plus, ArrowLeft, MoreHorizontal, Clock, User, Tag, MessageSquare } from 'lucide-react'
import { useState } from 'react'

interface Task {
  id: number
  title: string
  description: string
  status: string
  priority: string
  assignee: { name: string; id: number } | null
  due_date: string | null
  estimated_hours: number
  comment_count: number
  tags: { id: number; name: string; color: string }[]
}

interface Column {
  id: number
  name: string
  status_mapping: string
  color: string
  task_count: number
}

export default function Board() {
  const { boardId } = useParams()
  const [showTaskModal, setShowTaskModal] = useState(false)
  const [selectedColumn, setSelectedColumn] = useState<string>('todo')
  const queryClient = useQueryClient()

  const { data: boardData, isLoading: boardLoading } = useQuery({
    queryKey: ['board', boardId],
    queryFn: () => boardApi.getById(Number(boardId), { include_tasks: true }),
  })

  const { data: tasksData } = useQuery({
    queryKey: ['tasks', boardId],
    queryFn: () => taskApi.getAll({ board_id: Number(boardId), per_page: 200 }),
  })

  const reorderMutation = useMutation({
    mutationFn: (data: { task_orders: { id: number; position: number; status: string }[] }) =>
      taskApi.reorder(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['tasks', boardId] })
    },
  })

  const board = boardData?.data
  const tasks: Task[] = tasksData?.data?.tasks || []
  const columns: Column[] = board?.columns || []

  const getTasksByStatus = (status: string) =>
    tasks.filter((t) => t.status === status).sort((a, b) => a.id - b.id)

  const handleDragEnd = (result: DropResult) => {
    if (!result.destination) return

    const { source, destination, draggableId } = result
    const taskId = parseInt(draggableId.replace('task-', ''))
    const newStatus = destination.droppableId

    // Update task status
    taskApi.update(taskId, { status: newStatus })

    // Optimistically update the cache
    queryClient.setQueryData(['tasks', boardId], (old: unknown) => {
      if (!old || typeof old !== 'object') return old
      const data = old as { data: { tasks: Task[] } }
      return {
        ...data,
        data: {
          ...data.data,
          tasks: data.data.tasks.map((t: Task) =>
            t.id === taskId ? { ...t, status: newStatus } : t
          ),
        },
      }
    })
  }

  if (boardLoading) {
    return (
      <div className="animate-pulse space-y-6">
        <div className="h-8 bg-gray-200 rounded w-1/4"></div>
        <div className="flex gap-4">
          {[1, 2, 3, 4].map((i) => (
            <div key={i} className="w-80 h-96 bg-gray-200 rounded-xl"></div>
          ))}
        </div>
      </div>
    )
  }

  return (
    <div className="h-full">
      {/* Header */}
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-4">
          <Link
            to={`/projects/${board?.project_id}`}
            className="text-gray-500 hover:text-gray-700"
          >
            <ArrowLeft className="h-5 w-5" />
          </Link>
          <div>
            <h1 className="text-2xl font-bold text-gray-900">{board?.name}</h1>
            <p className="text-gray-500 text-sm">
              {tasks.length} tasks • {board?.view_type} view
            </p>
          </div>
        </div>
        <button
          onClick={() => {
            setSelectedColumn('todo')
            setShowTaskModal(true)
          }}
          className="flex items-center gap-2 px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700"
        >
          <Plus className="h-5 w-5" />
          Add Task
        </button>
      </div>

      {/* Kanban Board */}
      <DragDropContext onDragEnd={handleDragEnd}>
        <div className="flex gap-4 overflow-x-auto pb-4">
          {columns.map((column) => (
            <div
              key={column.id}
              className="flex-shrink-0 w-80 bg-gray-100 rounded-xl"
            >
              {/* Column Header */}
              <div className="p-4 border-b border-gray-200">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <div
                      className="w-3 h-3 rounded-full"
                      style={{ backgroundColor: column.color }}
                    />
                    <h3 className="font-semibold text-gray-900">{column.name}</h3>
                    <span className="px-2 py-0.5 bg-gray-200 rounded-full text-xs text-gray-600">
                      {getTasksByStatus(column.status_mapping).length}
                    </span>
                  </div>
                  <button
                    onClick={() => {
                      setSelectedColumn(column.status_mapping)
                      setShowTaskModal(true)
                    }}
                    className="p-1 hover:bg-gray-200 rounded"
                  >
                    <Plus className="h-4 w-4 text-gray-500" />
                  </button>
                </div>
              </div>

              {/* Column Content */}
              <Droppable droppableId={column.status_mapping}>
                {(provided, snapshot) => (
                  <div
                    ref={provided.innerRef}
                    {...provided.droppableProps}
                    className={`p-2 min-h-[200px] max-h-[calc(100vh-300px)] overflow-y-auto ${
                      snapshot.isDraggingOver ? 'bg-primary-50' : ''
                    }`}
                  >
                    {getTasksByStatus(column.status_mapping).map((task, index) => (
                      <Draggable
                        key={task.id}
                        draggableId={`task-${task.id}`}
                        index={index}
                      >
                        {(provided, snapshot) => (
                          <div
                            ref={provided.innerRef}
                            {...provided.draggableProps}
                            {...provided.dragHandleProps}
                            className={`task-card mb-2 ${
                              snapshot.isDragging ? 'shadow-lg' : ''
                            }`}
                          >
                            <TaskCard task={task} />
                          </div>
                        )}
                      </Draggable>
                    ))}
                    {provided.placeholder}
                  </div>
                )}
              </Droppable>
            </div>
          ))}
        </div>
      </DragDropContext>

      {/* Create Task Modal */}
      {showTaskModal && (
        <CreateTaskModal
          boardId={Number(boardId)}
          defaultStatus={selectedColumn}
          onClose={() => setShowTaskModal(false)}
        />
      )}
    </div>
  )
}

function TaskCard({ task }: { task: Task }) {
  const priorityColors: Record<string, string> = {
    low: 'bg-gray-100 text-gray-600',
    medium: 'bg-blue-100 text-blue-600',
    high: 'bg-yellow-100 text-yellow-600',
    critical: 'bg-red-100 text-red-600',
  }

  return (
    <div className="bg-white rounded-lg p-4 shadow-sm border border-gray-200 hover:border-primary-300">
      {/* Tags */}
      {task.tags.length > 0 && (
        <div className="flex flex-wrap gap-1 mb-2">
          {task.tags.slice(0, 3).map((tag) => (
            <span
              key={tag.id}
              className="px-2 py-0.5 rounded text-xs"
              style={{ backgroundColor: tag.color + '20', color: tag.color }}
            >
              {tag.name}
            </span>
          ))}
        </div>
      )}

      {/* Title */}
      <h4 className="font-medium text-gray-900 mb-2">{task.title}</h4>

      {/* Description preview */}
      {task.description && (
        <p className="text-sm text-gray-500 mb-3 line-clamp-2">{task.description}</p>
      )}

      {/* Meta */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          {/* Priority */}
          <span
            className={`px-2 py-0.5 rounded text-xs font-medium capitalize ${
              priorityColors[task.priority]
            }`}
          >
            {task.priority}
          </span>

          {/* Due date */}
          {task.due_date && (
            <span className="flex items-center gap-1 text-xs text-gray-500">
              <Clock className="h-3 w-3" />
              {new Date(task.due_date).toLocaleDateString()}
            </span>
          )}
        </div>

        <div className="flex items-center gap-2">
          {/* Comments */}
          {task.comment_count > 0 && (
            <span className="flex items-center gap-1 text-xs text-gray-500">
              <MessageSquare className="h-3 w-3" />
              {task.comment_count}
            </span>
          )}

          {/* Assignee */}
          {task.assignee && (
            <div
              className="h-6 w-6 rounded-full bg-primary-100 flex items-center justify-center"
              title={task.assignee.name}
            >
              <span className="text-xs font-medium text-primary-600">
                {task.assignee.name.charAt(0)}
              </span>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

function CreateTaskModal({
  boardId,
  defaultStatus,
  onClose,
}: {
  boardId: number
  defaultStatus: string
  onClose: () => void
}) {
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const [priority, setPriority] = useState('medium')
  const queryClient = useQueryClient()

  const createMutation = useMutation({
    mutationFn: (data: Record<string, unknown>) => taskApi.create(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['tasks', String(boardId)] })
      onClose()
    },
  })

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    createMutation.mutate({
      board_id: boardId,
      title,
      description,
      status: defaultStatus,
      priority,
    })
  }

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white rounded-xl shadow-xl w-full max-w-md p-6">
        <h2 className="text-xl font-bold text-gray-900 mb-4">Create New Task</h2>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Task Title *
            </label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
              placeholder="Enter task title"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Description
            </label>
            <textarea
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
              placeholder="Task description"
              rows={3}
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Priority
            </label>
            <select
              value={priority}
              onChange={(e) => setPriority(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
            >
              <option value="low">Low</option>
              <option value="medium">Medium</option>
              <option value="high">High</option>
              <option value="critical">Critical</option>
            </select>
          </div>

          <div className="flex gap-3 pt-4">
            <button
              type="button"
              onClick={onClose}
              className="flex-1 px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={createMutation.isPending}
              className="flex-1 px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 disabled:opacity-50"
            >
              {createMutation.isPending ? 'Creating...' : 'Create Task'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}
