import { useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import { reportApi, projectApi } from '../services/api'
import { BarChart3, PieChart, TrendingUp, Download } from 'lucide-react'
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, AreaChart, Area } from 'recharts'

export default function Reports() {
  const [selectedProject, setSelectedProject] = useState<number | null>(null)

  const { data: projectsData } = useQuery({
    queryKey: ['projects'],
    queryFn: () => projectApi.getAll(),
  })

  const { data: utilizationData } = useQuery({
    queryKey: ['resource-utilization'],
    queryFn: () => reportApi.getResourceUtilization(),
  })

  const { data: riskData } = useQuery({
    queryKey: ['risk-summary'],
    queryFn: () => reportApi.getRiskSummary(),
  })

  const { data: velocityData } = useQuery({
    queryKey: ['velocity', selectedProject],
    queryFn: () => reportApi.getVelocity({ project_id: selectedProject, weeks: 8 }),
    enabled: !!selectedProject,
  })

  const { data: burndownData } = useQuery({
    queryKey: ['burndown', selectedProject],
    queryFn: () => reportApi.getBurndown(selectedProject!),
    enabled: !!selectedProject,
  })

  const projects = projectsData?.data?.projects || []
  const utilization = utilizationData?.data?.utilization || []
  const risks = riskData?.data || {}
  const velocity = velocityData?.data?.velocity || []
  const burndown = burndownData?.data || {}

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Reports & Analytics</h1>
          <p className="text-gray-500">Insights and performance metrics</p>
        </div>
        <button className="flex items-center gap-2 px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50">
          <Download className="h-4 w-4" />
          Export
        </button>
      </div>

      {/* Project Selector */}
      <div className="bg-white rounded-xl shadow-sm p-6">
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Select Project for Detailed Reports
        </label>
        <select
          value={selectedProject || ''}
          onChange={(e) => setSelectedProject(e.target.value ? Number(e.target.value) : null)}
          className="w-full max-w-md px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option value="">Select a project...</option>
          {projects.map((p: { id: number; name: string }) => (
            <option key={p.id} value={p.id}>{p.name}</option>
          ))}
        </select>
      </div>

      {/* Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="bg-white rounded-xl shadow-sm p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-500">Total Risks</p>
              <p className="text-2xl font-bold">{risks.summary?.total_risks || 0}</p>
            </div>
            <div className="h-10 w-10 rounded-lg bg-yellow-100 flex items-center justify-center">
              <BarChart3 className="h-5 w-5 text-yellow-600" />
            </div>
          </div>
        </div>
        <div className="bg-white rounded-xl shadow-sm p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-500">Open Risks</p>
              <p className="text-2xl font-bold">{risks.summary?.open_risks || 0}</p>
            </div>
            <div className="h-10 w-10 rounded-lg bg-red-100 flex items-center justify-center">
              <PieChart className="h-5 w-5 text-red-600" />
            </div>
          </div>
        </div>
        <div className="bg-white rounded-xl shadow-sm p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-500">High/Critical</p>
              <p className="text-2xl font-bold">{risks.summary?.high_critical_risks || 0}</p>
            </div>
            <div className="h-10 w-10 rounded-lg bg-orange-100 flex items-center justify-center">
              <TrendingUp className="h-5 w-5 text-orange-600" />
            </div>
          </div>
        </div>
        <div className="bg-white rounded-xl shadow-sm p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-500">Avg Risk Score</p>
              <p className="text-2xl font-bold">{risks.summary?.average_score?.toFixed(1) || 0}</p>
            </div>
            <div className="h-10 w-10 rounded-lg bg-blue-100 flex items-center justify-center">
              <BarChart3 className="h-5 w-5 text-blue-600" />
            </div>
          </div>
        </div>
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Velocity Chart */}
        {selectedProject && velocity.length > 0 && (
          <div className="bg-white rounded-xl shadow-sm p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Team Velocity</h2>
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={velocity}>
                  <XAxis dataKey="week_start" tick={{ fontSize: 10 }} />
                  <YAxis tick={{ fontSize: 12 }} />
                  <Tooltip />
                  <Area
                    type="monotone"
                    dataKey="tasks_completed"
                    stroke="#6366F1"
                    fill="#6366F1"
                    fillOpacity={0.2}
                  />
                </AreaChart>
              </ResponsiveContainer>
            </div>
          </div>
        )}

        {/* Burndown Chart */}
        {selectedProject && burndown.actual_burndown && (
          <div className="bg-white rounded-xl shadow-sm p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Burndown Chart</h2>
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={burndown.actual_burndown}>
                  <XAxis dataKey="date" tick={{ fontSize: 10 }} />
                  <YAxis tick={{ fontSize: 12 }} />
                  <Tooltip />
                  <Line
                    type="monotone"
                    dataKey="remaining_points"
                    stroke="#EF4444"
                    strokeWidth={2}
                    dot={false}
                    name="Actual"
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </div>
        )}

        {/* Risk Trend */}
        {risks.trend && (
          <div className="bg-white rounded-xl shadow-sm p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Risk Trend</h2>
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={risks.trend}>
                  <XAxis dataKey="week" tick={{ fontSize: 10 }} />
                  <YAxis tick={{ fontSize: 12 }} />
                  <Tooltip />
                  <Area
                    type="monotone"
                    dataKey="new_risks"
                    stroke="#F59E0B"
                    fill="#F59E0B"
                    fillOpacity={0.2}
                  />
                </AreaChart>
              </ResponsiveContainer>
            </div>
          </div>
        )}

        {/* Resource Utilization Trend */}
        <div className="bg-white rounded-xl shadow-sm p-6">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">Team Utilization Overview</h2>
          <div className="space-y-4">
            {utilization.slice(0, 6).map((u: { user: { id: number; name: string }; utilization: number }) => (
              <div key={u.user.id} className="flex items-center gap-4">
                <div className="w-24 text-sm text-gray-600 truncate">{u.user.name}</div>
                <div className="flex-1 h-4 bg-gray-100 rounded-full overflow-hidden">
                  <div
                    className={`h-full rounded-full ${
                      u.utilization > 100 ? 'bg-red-500' :
                      u.utilization > 80 ? 'bg-yellow-500' : 'bg-green-500'
                    }`}
                    style={{ width: `${Math.min(u.utilization, 100)}%` }}
                  />
                </div>
                <div className="w-16 text-sm text-right font-medium">
                  {u.utilization}%
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Risk Level Breakdown */}
      {risks.level_breakdown && (
        <div className="bg-white rounded-xl shadow-sm p-6">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">Risk Level Breakdown</h2>
          <div className="grid grid-cols-4 gap-4">
            {Object.entries(risks.level_breakdown).map(([level, count]) => (
              <div key={level} className="p-4 bg-gray-50 rounded-lg text-center">
                <p className="text-2xl font-bold capitalize">{count as number}</p>
                <p className="text-sm text-gray-500 capitalize">{level}</p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
