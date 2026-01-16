# Project Manager Application - Architecture Design

## Overview

A comprehensive, self-hosted project management application for small teams, built with Python (Flask) backend and React frontend.

## Technology Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| Backend | Flask + Flask-RESTful | Lightweight, flexible Python framework |
| Database | SQLite | File-based, no setup, perfect for self-hosted |
| ORM | SQLAlchemy | Powerful Python ORM with migration support |
| API | REST + WebSocket | REST for CRUD, WebSocket for real-time |
| Frontend | React 18 | Modern component-based UI |
| UI Framework | Tailwind CSS + shadcn/ui | Clean, customizable design system |
| State Management | Zustand | Lightweight state management |
| Charts | Recharts | React-native charting library |
| Gantt | Custom + react-big-calendar | Timeline visualization |
| Real-time | Flask-SocketIO | WebSocket support for collaboration |

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        React Frontend                           │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │ Projects │ │ Boards   │ │ Reports  │ │ Settings │           │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘           │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              Zustand State Management                    │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │   REST API        │ WebSocket
                    │   /api/v1/*       │ /ws
                    └─────────┬─────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                      Flask Backend                              │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                   API Layer                              │   │
│  │  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐            │   │
│  │  │Projects│ │Tasks   │ │Users   │ │Reports │            │   │
│  │  └────────┘ └────────┘ └────────┘ └────────┘            │   │
│  └─────────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 Service Layer                            │   │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐           │   │
│  │  │Automation  │ │Critical    │ │Resource    │           │   │
│  │  │Engine      │ │Path Calc   │ │Allocator   │           │   │
│  │  └────────────┘ └────────────┘ └────────────┘           │   │
│  └─────────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              SQLAlchemy ORM + SQLite                     │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

## Data Model

### Core Entities

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│    Portfolio    │────<│    Program      │────<│    Project      │
├─────────────────┤     ├─────────────────┤     ├─────────────────┤
│ id              │     │ id              │     │ id              │
│ name            │     │ name            │     │ name            │
│ description     │     │ portfolio_id    │     │ program_id      │
│ owner_id        │     │ objectives[]    │     │ template_id     │
│ status          │     │ status          │     │ status          │
│ created_at      │     │ budget          │     │ start_date      │
└─────────────────┘     └─────────────────┘     │ end_date        │
                                                │ budget          │
                                                │ baseline_data   │
                                                └─────────────────┘
                                                        │
                        ┌───────────────────────────────┼───────────────────────────────┐
                        │                               │                               │
                        ▼                               ▼                               ▼
              ┌─────────────────┐            ┌─────────────────┐            ┌─────────────────┐
              │     Board       │            │   Milestone     │            │     Risk        │
              ├─────────────────┤            ├─────────────────┤            ├─────────────────┤
              │ id              │            │ id              │            │ id              │
              │ project_id      │            │ project_id      │            │ project_id      │
              │ name            │            │ name            │            │ title           │
              │ view_type       │            │ due_date        │            │ probability     │
              │ columns[]       │            │ status          │            │ impact          │
              └─────────────────┘            └─────────────────┘            │ owner_id        │
                        │                                                   │ mitigation      │
                        ▼                                                   │ status          │
              ┌─────────────────┐                                           └─────────────────┘
              │     Task        │
              ├─────────────────┤
              │ id              │
              │ board_id        │
              │ title           │
              │ description     │
              │ status          │
              │ priority        │
              │ assignee_id     │
              │ due_date        │
              │ estimated_hours │
              │ actual_hours    │
              │ dependencies[]  │
              │ tags[]          │
              └─────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│  Comment    │ │ Attachment  │ │ TimeEntry   │
└─────────────┘ └─────────────┘ └─────────────┘
```

### Supporting Entities

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│      User       │     │      Team       │     │   Automation    │
├─────────────────┤     ├─────────────────┤     ├─────────────────┤
│ id              │     │ id              │     │ id              │
│ email           │     │ name            │     │ name            │
│ name            │     │ members[]       │     │ trigger_type    │
│ role            │     │ capacity_rules  │     │ trigger_config  │
│ skills[]        │     └─────────────────┘     │ actions[]       │
│ capacity        │                             │ is_active       │
│ working_hours   │                             └─────────────────┘
└─────────────────┘

┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│    Template     │     │      OKR        │     │  Integration    │
├─────────────────┤     ├─────────────────┤     ├─────────────────┤
│ id              │     │ id              │     │ id              │
│ name            │     │ objective       │     │ type            │
│ category        │     │ key_results[]   │     │ config          │
│ structure       │     │ program_id      │     │ credentials     │
│ default_tasks[] │     │ progress        │     │ is_active       │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

## Feature Modules

### 1. Project Management
- **Visual Workspaces**: Boards with customizable columns
- **Multiple Views**: Kanban, Gantt, Calendar, Table
- **Templates**: Pre-built project templates
- **Collaboration**: Comments, mentions, file attachments

### 2. Advanced Project Management
- **Dependencies**: Task linking with predecessor/successor
- **Baseline Tracking**: Snapshot and compare planned vs actual
- **Critical Path**: Automatic calculation and visualization
- **Time Tracking**: Timer + manual entry

### 3. Program Management
- **Portfolio Dashboard**: Aggregate view of all projects
- **Cross-Project Dependencies**: Inter-project task linking
- **OKR Alignment**: Link projects to objectives
- **Executive Reports**: Auto-generated summaries

### 4. Resource Planning
- **Workload View**: Visual capacity indicators
- **Skill Matching**: Filter resources by skills
- **Forecasting**: Predict future workload
- **Capacity Rules**: Working hours, holidays

### 5. Resource Allocation
- **Drag-Drop Reallocation**: Easy reassignment
- **Load Indicators**: Color-coded utilization
- **Auto-Updates**: Allocation adjusts with timeline changes

### 6. Risk & Issue Management
- **Risk Register**: Centralized risk tracking
- **Custom Fields**: Probability, impact, mitigation
- **Risk Dashboard**: Heatmaps and trends
- **Linked Risks**: Connect to tasks/milestones

### 7. Automation & Integration
- **Automation Rules**: No-code workflow builder
- **Webhook Support**: External integrations
- **API**: RESTful API for custom integrations
- **AI Insights**: Delay prediction, workload recommendations

## API Structure

```
/api/v1/
├── /auth
│   ├── POST /login
│   ├── POST /logout
│   └── POST /register
├── /users
│   ├── GET /
│   ├── GET /:id
│   ├── PUT /:id
│   └── GET /:id/workload
├── /portfolios
│   ├── GET /
│   ├── POST /
│   ├── GET /:id
│   ├── PUT /:id
│   └── GET /:id/dashboard
├── /programs
│   ├── GET /
│   ├── POST /
│   ├── GET /:id
│   ├── PUT /:id
│   └── GET /:id/okrs
├── /projects
│   ├── GET /
│   ├── POST /
│   ├── GET /:id
│   ├── PUT /:id
│   ├── GET /:id/critical-path
│   ├── GET /:id/baseline
│   └── POST /:id/baseline
├── /boards
│   ├── GET /
│   ├── POST /
│   ├── GET /:id
│   └── PUT /:id
├── /tasks
│   ├── GET /
│   ├── POST /
│   ├── GET /:id
│   ├── PUT /:id
│   ├── POST /:id/dependencies
│   ├── GET /:id/comments
│   └── POST /:id/time-entries
├── /risks
│   ├── GET /
│   ├── POST /
│   ├── GET /:id
│   └── PUT /:id
├── /resources
│   ├── GET /workload
│   ├── GET /forecast
│   └── POST /allocate
├── /automations
│   ├── GET /
│   ├── POST /
│   ├── PUT /:id
│   └── POST /:id/test
├── /templates
│   ├── GET /
│   └── POST /apply/:id
└── /reports
    ├── GET /portfolio
    ├── GET /resource-utilization
    └── GET /risk-summary
```

## Directory Structure

```
project-manager/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── project.py
│   │   │   ├── task.py
│   │   │   ├── risk.py
│   │   │   └── automation.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── projects.py
│   │   │   ├── tasks.py
│   │   │   ├── resources.py
│   │   │   └── automations.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── critical_path.py
│   │   │   ├── automation_engine.py
│   │   │   ├── resource_allocator.py
│   │   │   └── ai_insights.py
│   │   └── utils/
│   │       ├── __init__.py
│   │       └── helpers.py
│   ├── migrations/
│   ├── tests/
│   ├── requirements.txt
│   └── run.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── boards/
│   │   │   ├── charts/
│   │   │   ├── common/
│   │   │   └── layout/
│   │   ├── pages/
│   │   │   ├── Dashboard.tsx
│   │   │   ├── Projects.tsx
│   │   │   ├── Board.tsx
│   │   │   ├── Resources.tsx
│   │   │   └── Reports.tsx
│   │   ├── stores/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── types/
│   │   └── utils/
│   ├── public/
│   ├── package.json
│   └── vite.config.ts
├── docker-compose.yml
├── README.md
└── ARCHITECTURE.md
```

## Security Considerations

1. **Authentication**: JWT-based with refresh tokens
2. **Authorization**: Role-based access control (RBAC)
3. **Data Validation**: Input sanitization on all endpoints
4. **CORS**: Configured for self-hosted deployment
5. **Rate Limiting**: API rate limiting per user

## Deployment

Self-hosted deployment options:
1. **Docker Compose**: Single command deployment
2. **Manual**: Python + Node.js on any server
3. **Reverse Proxy**: Nginx for production

## Performance Considerations

1. **Pagination**: All list endpoints paginated
2. **Caching**: Redis optional for session/cache
3. **Lazy Loading**: Frontend lazy loads heavy components
4. **Database Indexing**: Optimized queries with proper indexes
