import { useState } from 'react'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { riskApi, projectApi } from '../services/api'
import { Plus, AlertTriangle, Search, Filter } from 'lucide-react'

interface Risk {
  id: number
  title: string
  description: string
  category: string
  probability: string
  impact: string
  risk_score: number
  risk_level: string
  status: string
  owner: { name: string } | null
  project_id: number
}

export default function Risks() {
  const [searchQuery, setSearchQuery] = useState('')
  const [statusFilter, setStatusFilter] = useState('')
  const [showCreateModal, setShowCreateModal] = useState(false)
  const queryClient = useQueryClient()

  const { data: risksData, isLoading } = useQuery({
    queryKey: ['risks', statusFilter],
    queryFn: () => riskApi.getAll({ status: statusFilter || undefined }),
  })

  const { data: matrixData } = useQuery({
    queryKey: ['risk-matrix'],
    queryFn: () => riskApi.getMatrix(),
  })

  const risks: Risk[] = risksData?.data?.risks || []
  const matrix = matrixData?.data?.matrix || {}

  const filteredRisks = risks.filter(
    (r) => r.title.toLowerCase().includes(searchQuery.toLowerCase())
  )

  const levelColors: Record<string, string> = {
    low: 'bg-green-100 text-green-700',
    medium: 'bg-yellow-100 text-yellow-700',
    high: 'bg-orange-100 text-orange-700',
    critical: 'bg-red-100 text-red-700',
  }

  const statusColors: Record<string, string> = {
    identified: 'bg-gray-100 text-gray-700',
    analyzing: 'bg-blue-100 text-blue-700',
    mitigating: 'bg-yellow-100 text-yellow-700',
    monitoring: 'bg-purple-100 text-purple-700',
    resolved: 'bg-green-100 text-green-700',
    closed: 'bg-gray-100 text-gray-700',
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Risk Management</h1>
          <p className="text-gray-500">Track and manage project risks</p>
        </div>
        <button
          onClick={() => setShowCreateModal(true)}
          className="flex items-center gap-2 px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700"
        >
          <Plus className="h-5 w-5" />
          New Risk
        </button>
      </div>

      {/* Risk Matrix */}
      <div className="bg-white rounded-xl shadow-sm p-6">
        <h2 className="text-lg font-semibold text-gray-900 mb-4">Risk Heat Map</h2>
        <div className="overflow-x-auto">
          <table className="w-full border-collapse">
            <thead>
              <tr>
                <th className="p-2 text-xs text-gray-500"></th>
                {['very_low', 'low', 'medium', 'high', 'very_high'].map((impact) => (
                  <th key={impact} className="p-2 text-xs text-gray-500 capitalize">
                    {impact.replace('_', ' ')}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {['very_high', 'high', 'medium', 'low', 'very_low'].map((prob) => (
                <tr key={prob}>
                  <td className="p-2 text-xs text-gray-500 capitalize font-medium">
                    {prob.replace('_', ' ')}
                  </td>
                  {['very_low', 'low', 'medium', 'high', 'very_high'].map((impact) => {
                    const cellRisks = matrix[prob]?.[impact] || []
                    const probVal = { very_low: 1, low: 2, medium: 3, high: 4, very_high: 5 }[prob]
                    const impactVal = { very_low: 1, low: 2, medium: 3, high: 4, very_high: 5 }[impact]
                    const score = (probVal || 0) * (impactVal || 0)
                    const bgColor = score <= 4 ? 'bg-green-100' :
                                   score <= 9 ? 'bg-yellow-100' :
                                   score <= 15 ? 'bg-orange-100' : 'bg-red-100'
                    return (
                      <td
                        key={`${prob}-${impact}`}
                        className={`p-2 text-center ${bgColor} border border-white`}
                      >
                        {cellRisks.length > 0 && (
                          <span className="inline-flex items-center justify-center h-6 w-6 rounded-full bg-white text-xs font-medium">
                            {cellRisks.length}
                          </span>
                        )}
                      </td>
                    )
                  })}
                </tr>
              ))}
            </tbody>
          </table>
          <div className="flex items-center gap-4 mt-4 text-xs">
            <span className="flex items-center gap-1">
              <span className="w-4 h-4 bg-green-100 rounded"></span> Low
            </span>
            <span className="flex items-center gap-1">
              <span className="w-4 h-4 bg-yellow-100 rounded"></span> Medium
            </span>
            <span className="flex items-center gap-1">
              <span className="w-4 h-4 bg-orange-100 rounded"></span> High
            </span>
            <span className="flex items-center gap-1">
              <span className="w-4 h-4 bg-red-100 rounded"></span> Critical
            </span>
          </div>
        </div>
      </div>

      {/* Filters */}
      <div className="flex items-center gap-4">
        <div className="flex-1 max-w-md relative">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-400" />
          <input
            type="text"
            placeholder="Search risks..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-10 pr-4 py-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
        </div>
        <select
          value={statusFilter}
          onChange={(e) => setStatusFilter(e.target.value)}
          className="px-4 py-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
        >
          <option value="">All Status</option>
          <option value="identified">Identified</option>
          <option value="analyzing">Analyzing</option>
          <option value="mitigating">Mitigating</option>
          <option value="monitoring">Monitoring</option>
          <option value="resolved">Resolved</option>
        </select>
      </div>

      {/* Risks List */}
      <div className="bg-white rounded-xl shadow-sm overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                Risk
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                Category
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                Level
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                Score
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                Status
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                Owner
              </th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {filteredRisks.map((risk) => (
              <tr key={risk.id} className="hover:bg-gray-50 cursor-pointer">
                <td className="px-6 py-4">
                  <div className="flex items-center gap-3">
                    <AlertTriangle className={`h-5 w-5 ${
                      risk.risk_level === 'critical' ? 'text-red-500' :
                      risk.risk_level === 'high' ? 'text-orange-500' :
                      risk.risk_level === 'medium' ? 'text-yellow-500' : 'text-green-500'
                    }`} />
                    <div>
                      <p className="font-medium text-gray-900">{risk.title}</p>
                      {risk.description && (
                        <p className="text-sm text-gray-500 truncate max-w-xs">
                          {risk.description}
                        </p>
                      )}
                    </div>
                  </div>
                </td>
                <td className="px-6 py-4 text-gray-500 capitalize">
                  {risk.category || '-'}
                </td>
                <td className="px-6 py-4">
                  <span className={`px-2 py-1 rounded-full text-xs font-medium capitalize ${
                    levelColors[risk.risk_level]
                  }`}>
                    {risk.risk_level}
                  </span>
                </td>
                <td className="px-6 py-4 font-medium">{risk.risk_score}</td>
                <td className="px-6 py-4">
                  <span className={`px-2 py-1 rounded-full text-xs font-medium capitalize ${
                    statusColors[risk.status]
                  }`}>
                    {risk.status}
                  </span>
                </td>
                <td className="px-6 py-4 text-gray-500">
                  {risk.owner?.name || 'Unassigned'}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Create Risk Modal */}
      {showCreateModal && (
        <CreateRiskModal onClose={() => setShowCreateModal(false)} />
      )}
    </div>
  )
}

function CreateRiskModal({ onClose }: { onClose: () => void }) {
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const [probability, setProbability] = useState('medium')
  const [impact, setImpact] = useState('medium')
  const [projectId, setProjectId] = useState<number | null>(null)
  const queryClient = useQueryClient()

  const { data: projectsData } = useQuery({
    queryKey: ['projects'],
    queryFn: () => projectApi.getAll(),
  })

  const projects = projectsData?.data?.projects || []

  const createMutation = useMutation({
    mutationFn: (data: Record<string, unknown>) => riskApi.create(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['risks'] })
      queryClient.invalidateQueries({ queryKey: ['risk-matrix'] })
      onClose()
    },
  })

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (!projectId) return
    createMutation.mutate({
      project_id: projectId,
      title,
      description,
      probability,
      impact,
    })
  }

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white rounded-xl shadow-xl w-full max-w-md p-6">
        <h2 className="text-xl font-bold text-gray-900 mb-4">Create New Risk</h2>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Project *
            </label>
            <select
              value={projectId || ''}
              onChange={(e) => setProjectId(Number(e.target.value))}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
              required
            >
              <option value="">Select project...</option>
              {projects.map((p: { id: number; name: string }) => (
                <option key={p.id} value={p.id}>{p.name}</option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Risk Title *
            </label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
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
              rows={3}
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Probability
              </label>
              <select
                value={probability}
                onChange={(e) => setProbability(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg"
              >
                <option value="very_low">Very Low</option>
                <option value="low">Low</option>
                <option value="medium">Medium</option>
                <option value="high">High</option>
                <option value="very_high">Very High</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Impact
              </label>
              <select
                value={impact}
                onChange={(e) => setImpact(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg"
              >
                <option value="very_low">Very Low</option>
                <option value="low">Low</option>
                <option value="medium">Medium</option>
                <option value="high">High</option>
                <option value="very_high">Very High</option>
              </select>
            </div>
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
              {createMutation.isPending ? 'Creating...' : 'Create Risk'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}
