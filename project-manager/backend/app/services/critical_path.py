"""
Critical Path Calculator - Calculates critical path for project tasks
"""
from datetime import timedelta
from collections import defaultdict


class CriticalPathCalculator:
    """
    Calculates the critical path for a project using the Critical Path Method (CPM).
    The critical path is the longest sequence of dependent tasks that determines
    the minimum project duration.
    """

    def __init__(self, project):
        self.project = project
        self.tasks = []
        self.task_map = {}
        self.dependencies = defaultdict(list)
        self.dependents = defaultdict(list)

        self._load_tasks()

    def _load_tasks(self):
        """Load all tasks from the project"""
        for board in self.project.boards:
            for task in board.tasks:
                if task.status != 'cancelled':
                    self.tasks.append(task)
                    self.task_map[task.id] = {
                        'task': task,
                        'duration': task.estimated_hours or 0,
                        'early_start': 0,
                        'early_finish': 0,
                        'late_start': float('inf'),
                        'late_finish': float('inf'),
                        'slack': 0,
                        'is_critical': False
                    }

                    # Build dependency graph
                    for dep in task.dependencies:
                        self.dependencies[task.id].append(dep.depends_on_id)
                        self.dependents[dep.depends_on_id].append(task.id)

    def calculate(self):
        """
        Calculate the critical path using forward and backward pass.
        Returns critical path information.
        """
        if not self.tasks:
            return {
                'critical_path': [],
                'project_duration': 0,
                'tasks': []
            }

        # Forward pass - calculate early start and early finish
        self._forward_pass()

        # Find project duration (maximum early finish)
        project_duration = max(
            t['early_finish'] for t in self.task_map.values()
        ) if self.task_map else 0

        # Backward pass - calculate late start and late finish
        self._backward_pass(project_duration)

        # Calculate slack and identify critical tasks
        self._calculate_slack()

        # Build critical path
        critical_path = self._build_critical_path()

        # Prepare results
        tasks_data = []
        for task_id, data in self.task_map.items():
            task = data['task']
            tasks_data.append({
                'id': task.id,
                'title': task.title,
                'duration': data['duration'],
                'early_start': data['early_start'],
                'early_finish': data['early_finish'],
                'late_start': data['late_start'],
                'late_finish': data['late_finish'],
                'slack': data['slack'],
                'is_critical': data['is_critical'],
                'status': task.status,
                'dependencies': [d.depends_on_id for d in task.dependencies]
            })

        return {
            'critical_path': critical_path,
            'project_duration': project_duration,
            'tasks': tasks_data,
            'critical_tasks_count': sum(1 for t in tasks_data if t['is_critical']),
            'bottlenecks': self._identify_bottlenecks(tasks_data)
        }

    def _forward_pass(self):
        """
        Forward pass: Calculate early start (ES) and early finish (EF).
        ES = max(EF of all predecessors)
        EF = ES + duration
        """
        # Topological sort
        sorted_tasks = self._topological_sort()

        for task_id in sorted_tasks:
            data = self.task_map[task_id]

            # Early start is the maximum early finish of all predecessors
            predecessors = self.dependencies[task_id]
            if predecessors:
                data['early_start'] = max(
                    self.task_map[pred_id]['early_finish']
                    for pred_id in predecessors
                    if pred_id in self.task_map
                )
            else:
                data['early_start'] = 0

            # Early finish = early start + duration
            data['early_finish'] = data['early_start'] + data['duration']

    def _backward_pass(self, project_duration):
        """
        Backward pass: Calculate late start (LS) and late finish (LF).
        LF = min(LS of all successors) or project_duration for ending tasks
        LS = LF - duration
        """
        # Reverse topological order
        sorted_tasks = self._topological_sort()
        sorted_tasks.reverse()

        for task_id in sorted_tasks:
            data = self.task_map[task_id]

            # Late finish is the minimum late start of all successors
            successors = self.dependents[task_id]
            valid_successors = [s for s in successors if s in self.task_map]

            if valid_successors:
                data['late_finish'] = min(
                    self.task_map[succ_id]['late_start']
                    for succ_id in valid_successors
                )
            else:
                # Ending task - late finish equals project duration
                data['late_finish'] = project_duration

            # Late start = late finish - duration
            data['late_start'] = data['late_finish'] - data['duration']

    def _calculate_slack(self):
        """
        Calculate slack (float) for each task.
        Slack = LS - ES = LF - EF
        Tasks with zero slack are on the critical path.
        """
        for data in self.task_map.values():
            data['slack'] = data['late_start'] - data['early_start']
            data['is_critical'] = abs(data['slack']) < 0.001  # Nearly zero

    def _build_critical_path(self):
        """Build the critical path from critical tasks"""
        critical_tasks = [
            task_id for task_id, data in self.task_map.items()
            if data['is_critical']
        ]

        # Sort by early start to get the path order
        critical_tasks.sort(key=lambda t: self.task_map[t]['early_start'])

        return [{
            'id': task_id,
            'title': self.task_map[task_id]['task'].title,
            'duration': self.task_map[task_id]['duration'],
            'early_start': self.task_map[task_id]['early_start'],
            'early_finish': self.task_map[task_id]['early_finish']
        } for task_id in critical_tasks]

    def _topological_sort(self):
        """
        Topological sort of tasks based on dependencies.
        Uses Kahn's algorithm.
        """
        in_degree = defaultdict(int)
        for task_id in self.task_map:
            in_degree[task_id] = 0

        for task_id in self.task_map:
            for pred_id in self.dependencies[task_id]:
                if pred_id in self.task_map:
                    in_degree[task_id] += 1

        # Start with tasks that have no dependencies
        queue = [t for t in self.task_map if in_degree[t] == 0]
        sorted_tasks = []

        while queue:
            task_id = queue.pop(0)
            sorted_tasks.append(task_id)

            for succ_id in self.dependents[task_id]:
                if succ_id in self.task_map:
                    in_degree[succ_id] -= 1
                    if in_degree[succ_id] == 0:
                        queue.append(succ_id)

        # Handle any remaining tasks (circular dependencies)
        for task_id in self.task_map:
            if task_id not in sorted_tasks:
                sorted_tasks.append(task_id)

        return sorted_tasks

    def _identify_bottlenecks(self, tasks_data):
        """Identify potential bottlenecks in the project"""
        bottlenecks = []

        for task in tasks_data:
            # Critical tasks with many dependents are bottlenecks
            if task['is_critical']:
                dependent_count = len(self.dependents[task['id']])
                if dependent_count >= 2:
                    bottlenecks.append({
                        'task_id': task['id'],
                        'title': task['title'],
                        'reason': f'Critical task with {dependent_count} dependent tasks',
                        'severity': 'high' if dependent_count >= 3 else 'medium'
                    })

            # Tasks with low slack but not critical could become critical
            elif 0 < task['slack'] <= task['duration'] * 0.1:
                bottlenecks.append({
                    'task_id': task['id'],
                    'title': task['title'],
                    'reason': f'Near-critical task with only {task["slack"]:.1f}h slack',
                    'severity': 'medium'
                })

        return bottlenecks

    def get_schedule_impact(self, task_id, delay_hours):
        """
        Calculate the impact of delaying a specific task.
        """
        if task_id not in self.task_map:
            return {'error': 'Task not found'}

        task_data = self.task_map[task_id]

        if delay_hours <= task_data['slack']:
            return {
                'project_delay': 0,
                'affected_tasks': [],
                'message': 'Delay is within slack, no project impact'
            }

        # Delay exceeds slack
        project_delay = delay_hours - task_data['slack']
        affected = []

        # Find all downstream tasks
        def find_downstream(tid, visited=None):
            if visited is None:
                visited = set()
            if tid in visited:
                return []
            visited.add(tid)
            result = [tid]
            for succ_id in self.dependents[tid]:
                if succ_id in self.task_map:
                    result.extend(find_downstream(succ_id, visited))
            return result

        downstream = find_downstream(task_id)
        for tid in downstream:
            if tid != task_id and tid in self.task_map:
                affected.append({
                    'id': tid,
                    'title': self.task_map[tid]['task'].title
                })

        return {
            'project_delay': project_delay if task_data['is_critical'] else 0,
            'affected_tasks': affected,
            'message': f'Task is {"on" if task_data["is_critical"] else "not on"} critical path'
        }
