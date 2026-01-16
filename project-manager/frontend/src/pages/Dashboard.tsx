import { useQuery } from '@tanstack/react-query'
import { projectApi, taskApi, resourceApi } from '../services/api'
import {
  FolderKanban,
  CheckCircle2,
  Clock,
  AlertTriangle,
  TrendingUp,
  Users,
} from 'lucide-react'
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts'
import { Link } from 'react-router-dom'

const COLORS = ['#10B981', '#3B82F6', '#F59E0B', '#EF4444']

export default function Dashboard() {
  const { data: projectsData } = useQuery({
    queryKey: ['projects'],
    queryFn: () => projectApi.getAll({ per_page: 100 }),
  })

  const { data: tasksData } = useQuery({
    queryKey: ['tasks'],
    queryFn: () => taskApi.getAll({ per_page: 100 }),
  })

  const { data: workloadData } = useQuery({
    queryKey: ['workload'],
    queryFn: () => resourceApi.getWorkload(),
  })

  const projects = projectsData?.data?.projects || []
  const tasks = tasksData?.data?.tasks || []
  const workload = workloadData?.data?.workload || []

  // Calculate stats
  const totalProjects = projects.length
  const activeProjects = projects.filter((p: { status: string }) => p.status === 'active').length
  const completedTasks = tasks.filter((t: { status: string }) => t.status === 'completed').length
  const pendingTasks = tasks.filter((t: { status: string }) => t.status !== 'completed').length
  const overdueTasks = tasks.filter((t: { due_date: string; status: string }) => {
    if (!t.due_date || t.status === 'completed') return false
    return new Date(t.due_date) < new Date()
  }).length

  // Status distribution for pie chart
  const statusData = [
    { name: 'Completed', value: completedTasks },
    { name: 'In Progress', value: tasks.filter((t: { status: string }) => t.status === 'in_progress').length },
    { name: 'To Do', value: tasks.filter((t: { status: string }) => t.status === 'todo').length },
    { name: 'Blocked', value: tasks.filter((t: { status: string }) => t.status === 'blocked').length },
  ]

  // Project progress data for bar chart
  const projectProgressData = projects.slice(0, 6).map((p: { name: string; progress: number }) => ({
    name: p.name.length > 15 ? p.name.substring(0, 15) + '...' : p.name,
    progress: p.progress || 0,
  }))

  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h1 className="text-2xl font-bold text-gray-900">Dashboard</h1>
        <p className="text-gray-500">Welcome back! Here's your project overview.</p>
      </div>

      {/* Stats cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <StatCard
          title="Total Projects"
          value={totalProjects}
          icon={FolderKanban}
          color="bg-primary-500"
          subtext={`${activeProjects} active`}
        />
        <StatCard
          title="Completed Tasks"
          value={completedTasks}
          icon={CheckCircle2}
          color="bg-green-500"
          subtext={`of ${tasks.length} total`}
        />
        <StatCard
          title="Pending Tasks"
          value={pendingTasks}
          icon={Clock}
          color="bg-yellow-500"
          subtext={`${overdueTasks} overdue`}
        />
        <StatCard
          title="Team Members"
          value={workload.length}
          icon={Users}
          color="bg-blue-500"
          subtext="active users"
        />
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Project Progress */}
        <div className="bg-white rounded-xl shadow-sm p-6">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">Project Progress</h2>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={projectProgressData}>
                <XAxis dataKey="name" tick={{ fontSize: 12 }} />
                <YAxis domain={[0, 100]} tick={{ fontSize: 12 }} />
                <Tooltip />
                <Bar dataKey="progress" fill="#6366F1" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Task Distribution */}
        <div className="bg-white rounded-xl shadow-sm p-6">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">Task Distribution</h2>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={statusData}
                  cx="50%"
                  cy="50%"
                  innerRadius={60}
                  outerRadius={80}
                  paddingAngle={5}
                  dataKey="value"
                  label={({ name, value }) => `${name}: ${value}`}
                >
                  {statusData.map((_, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* Recent Projects and Team Workload */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Recent Projects */}
        <div className="bg-white rounded-xl shadow-sm p-6">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-lg font-semibold text-gray-900">Recent Projects</h2>
            <Link to="/projects" className="text-primary-600 text-sm hover:underline">
              View all
            </Link>
          </div>
          <div className="space-y-3">
            {projects.slice(0, 5).map((project: { id: number; name: string; status: string; progress: number }) => (
              <Link
                key={project.id}
                to={`/projects/${project.id}`}
                className="flex items-center justify-between p-3 rounded-lg hover:bg-gray-50 transition-colors"
              >
                <div className="flex items-center gap-3">
                  <div className="h-10 w-10 rounded-lg bg-primary-100 flex items-center justify-center">
                    <FolderKanban className="h-5 w-5 text-primary-600" />
                  </div>
                  <div>
                    <p className="font-medium text-gray-900">{project.name}</p>
                    <p className="text-sm text-gray-500 capitalize">{project.status}</p>
                  </div>
                </div>
                <div className="text-right">
                  <p className="font-medium text-gray-900">{project.progress || 0}%</p>
                  <div className="w-20 h-1.5 bg-gray-200 rounded-full mt-1">
                    <div
                      className="h-full bg-primary-500 rounded-full"
                      style={{ width: `${project.progress || 0}%` }}
                    />
                  </div>
                </div>
              </Link>
            ))}
          </div>
        </div>

        {/* Team Workload */}
        <div className="bg-white rounded-xl shadow-sm p-6">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-lg font-semibold text-gray-900">Team Workload</h2>
            <Link to="/resources" className="text-primary-600 text-sm hover:underline">
              View all
            </Link>
          </div>
          <div className="space-y-3">
            {workload.slice(0, 5).map((member: { user: { id: number; name: string }; utilization_percentage: number; status: string }) => (
              <div
                key={member.user.id}
                className="flex items-center justify-between p-3 rounded-lg hover:bg-gray-50"
              >
                <div className="flex items-center gap-3">
                  <div className="h-10 w-10 rounded-full bg-gray-100 flex items-center justify-center">
                    <span className="font-medium text-gray-600">
                      {member.user.name.charAt(0)}
                    </span>
                  </div>
                  <div>
                    <p className="font-medium text-gray-900">{member.user.name}</p>
                    <p className="text-sm text-gray-500 capitalize">{member.status}</p>
                  </div>
                </div>
                <div className="text-right">
                  <p className={`font-medium ${
                    member.utilization_percentage > 100 ? 'text-red-500' :
                    member.utilization_percentage > 80 ? 'text-yellow-500' : 'text-green-500'
                  }`}>
                    {member.utilization_percentage}%
                  </p>
                  <div className="w-20 h-1.5 bg-gray-200 rounded-full mt-1">
                    <div
                      className={`h-full rounded-full ${
                        member.utilization_percentage > 100 ? 'bg-red-500' :
                        member.utilization_percentage > 80 ? 'bg-yellow-500' : 'bg-green-500'
                      }`}
                      style={{ width: `${Math.min(member.utilization_percentage, 100)}%` }}
                    />
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}

function StatCard({
  title,
  value,
  icon: Icon,
  color,
  subtext,
}: {
  title: string
  value: number
  icon: React.ElementType
  color: string
  subtext: string
}) {
  return (
    <div className="bg-white rounded-xl shadow-sm p-6">
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm text-gray-500">{title}</p>
          <p className="text-3xl font-bold text-gray-900 mt-1">{value}</p>
          <p className="text-sm text-gray-500 mt-1">{subtext}</p>
        </div>
        <div className={`h-12 w-12 rounded-xl ${color} flex items-center justify-center`}>
          <Icon className="h-6 w-6 text-white" />
        </div>
      </div>
    </div>
  )
}
