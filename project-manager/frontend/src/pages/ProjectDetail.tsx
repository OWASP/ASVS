import { useParams, Link } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { projectApi, boardApi } from '../services/api'
import {
  ArrowLeft,
  Calendar,
  Users,
  Target,
  Clock,
  AlertTriangle,
  BarChart3,
  Kanban,
  GanttChart,
  Table,
  Plus,
} from 'lucide-react'
import { useState } from 'react'

export default function ProjectDetail() {
  const { projectId } = useParams()
  const [activeTab, setActiveTab] = useState('overview')

  const { data: projectData, isLoading } = useQuery({
    queryKey: ['project', projectId],
    queryFn: () => projectApi.getById(Number(projectId)),
  })

  const { data: boardsData } = useQuery({
    queryKey: ['boards', projectId],
    queryFn: () => boardApi.getAll({ project_id: Number(projectId) }),
  })

  const { data: criticalPathData } = useQuery({
    queryKey: ['critical-path', projectId],
    queryFn: () => projectApi.getCriticalPath(Number(projectId)),
    enabled: activeTab === 'critical-path',
  })

  const project = projectData?.data
  const boards = boardsData?.data || []
  const criticalPath = criticalPathData?.data

  if (isLoading) {
    return (
      <div className="animate-pulse space-y-6">
        <div className="h-8 bg-gray-200 rounded w-1/4"></div>
        <div className="h-32 bg-gray-200 rounded"></div>
      </div>
    )
  }

  if (!project) {
    return <div>Project not found</div>
  }

  const tabs = [
    { id: 'overview', label: 'Overview', icon: BarChart3 },
    { id: 'boards', label: 'Boards', icon: Kanban },
    { id: 'timeline', label: 'Timeline', icon: GanttChart },
    { id: 'critical-path', label: 'Critical Path', icon: Target },
    { id: 'risks', label: 'Risks', icon: AlertTriangle },
  ]

  return (
    <div className="space-y-6">
      {/* Back link */}
      <Link
        to="/projects"
        className="inline-flex items-center gap-2 text-gray-500 hover:text-gray-700"
      >
        <ArrowLeft className="h-4 w-4" />
        Back to Projects
      </Link>

      {/* Project Header */}
      <div className="bg-white rounded-xl shadow-sm p-6">
        <div className="flex items-start justify-between">
          <div>
            <div className="flex items-center gap-3 mb-2">
              <h1 className="text-2xl font-bold text-gray-900">{project.name}</h1>
              <span className="px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm font-medium capitalize">
                {project.status}
              </span>
            </div>
            <p className="text-gray-500">{project.description}</p>
          </div>
          <div className="flex items-center gap-2">
            <button className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50">
              Edit
            </button>
          </div>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-4 gap-6 mt-6 pt-6 border-t">
          <div>
            <p className="text-sm text-gray-500">Progress</p>
            <div className="flex items-center gap-2 mt-1">
              <div className="flex-1 h-2 bg-gray-200 rounded-full">
                <div
                  className="h-full bg-primary-500 rounded-full"
                  style={{ width: `${project.progress || 0}%` }}
                />
              </div>
              <span className="text-sm font-medium">{project.progress || 0}%</span>
            </div>
          </div>
          <div>
            <p className="text-sm text-gray-500">Tasks</p>
            <p className="text-xl font-semibold mt-1">
              {project.completed_task_count || 0} / {project.task_count || 0}
            </p>
          </div>
          <div>
            <p className="text-sm text-gray-500">Start Date</p>
            <p className="text-xl font-semibold mt-1">
              {project.start_date
                ? new Date(project.start_date).toLocaleDateString()
                : '-'}
            </p>
          </div>
          <div>
            <p className="text-sm text-gray-500">End Date</p>
            <p className="text-xl font-semibold mt-1">
              {project.target_end_date
                ? new Date(project.target_end_date).toLocaleDateString()
                : '-'}
            </p>
          </div>
        </div>
      </div>

      {/* Tabs */}
      <div className="bg-white rounded-xl shadow-sm">
        <div className="border-b px-6">
          <nav className="flex gap-6">
            {tabs.map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`flex items-center gap-2 py-4 border-b-2 text-sm font-medium transition-colors ${
                  activeTab === tab.id
                    ? 'border-primary-500 text-primary-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700'
                }`}
              >
                <tab.icon className="h-4 w-4" />
                {tab.label}
              </button>
            ))}
          </nav>
        </div>

        <div className="p-6">
          {activeTab === 'overview' && (
            <div className="space-y-6">
              <h3 className="font-semibold text-gray-900">Project Overview</h3>
              <div className="grid grid-cols-2 gap-6">
                <div className="p-4 bg-gray-50 rounded-lg">
                  <h4 className="font-medium text-gray-700 mb-2">Budget</h4>
                  <p className="text-2xl font-bold">${project.budget || 0}</p>
                  <p className="text-sm text-gray-500">
                    Spent: ${project.actual_cost || 0}
                  </p>
                </div>
                <div className="p-4 bg-gray-50 rounded-lg">
                  <h4 className="font-medium text-gray-700 mb-2">Owner</h4>
                  <p className="text-lg font-semibold">
                    {project.owner?.name || 'Unassigned'}
                  </p>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'boards' && (
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <h3 className="font-semibold text-gray-900">Project Boards</h3>
                <button className="flex items-center gap-2 px-3 py-1.5 bg-primary-600 text-white rounded-lg text-sm">
                  <Plus className="h-4 w-4" />
                  New Board
                </button>
              </div>
              <div className="grid grid-cols-2 gap-4">
                {boards.map((board: { id: number; name: string; view_type: string; task_count: number }) => (
                  <Link
                    key={board.id}
                    to={`/boards/${board.id}`}
                    className="p-4 border rounded-lg hover:border-primary-500 transition-colors"
                  >
                    <div className="flex items-center gap-3">
                      <Kanban className="h-8 w-8 text-primary-500" />
                      <div>
                        <h4 className="font-medium">{board.name}</h4>
                        <p className="text-sm text-gray-500 capitalize">
                          {board.view_type} • {board.task_count} tasks
                        </p>
                      </div>
                    </div>
                  </Link>
                ))}
              </div>
            </div>
          )}

          {activeTab === 'critical-path' && criticalPath && (
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <h3 className="font-semibold text-gray-900">Critical Path Analysis</h3>
                <div className="text-sm text-gray-500">
                  Project Duration: {criticalPath.project_duration} hours
                </div>
              </div>
              <div className="p-4 bg-red-50 rounded-lg border border-red-200">
                <h4 className="font-medium text-red-800 mb-2">
                  Critical Tasks ({criticalPath.critical_tasks_count})
                </h4>
                <div className="space-y-2">
                  {criticalPath.critical_path?.map((task: { id: number; title: string; duration: number }) => (
                    <div
                      key={task.id}
                      className="flex items-center justify-between p-2 bg-white rounded"
                    >
                      <span>{task.title}</span>
                      <span className="text-sm text-gray-500">
                        {task.duration}h
                      </span>
                    </div>
                  ))}
                </div>
              </div>
              {criticalPath.bottlenecks?.length > 0 && (
                <div className="p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                  <h4 className="font-medium text-yellow-800 mb-2">
                    Potential Bottlenecks
                  </h4>
                  <div className="space-y-2">
                    {criticalPath.bottlenecks.map((b: { task_id: number; title: string; reason: string }) => (
                      <div key={b.task_id} className="text-sm">
                        <span className="font-medium">{b.title}</span>: {b.reason}
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}

          {activeTab === 'timeline' && (
            <div className="text-center py-12 text-gray-500">
              Gantt chart timeline view coming soon
            </div>
          )}

          {activeTab === 'risks' && (
            <div className="text-center py-12 text-gray-500">
              Risk management view coming soon
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
