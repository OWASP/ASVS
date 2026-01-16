# Project Manager Application

A comprehensive, self-hosted project management application for small teams, featuring advanced project management capabilities including dependency tracking, critical path analysis, resource planning, risk management, and workflow automation.

## Features

### 1. Project Management
- Visual workspaces with customizable boards
- Multiple views: Kanban, Timeline (Gantt), Calendar, Table
- Task management with drag-and-drop
- Collaboration hub with comments and mentions
- File attachments
- Ready-to-use project templates

### 2. Advanced Project Management
- Dependency management (predecessor/successor relationships)
- Baseline tracking (planned vs. actual comparison)
- Critical path calculation and visualization
- Time tracking (timer + manual entry)
- Advanced dashboards and KPIs

### 3. Program Management
- Portfolio dashboards with aggregated views
- Cross-project dependency tracking
- OKR & Goal alignment
- Executive reporting

### 4. Resource Planning
- Workload visualization
- Skill-based assignment
- Capacity forecasting
- Custom capacity rules (working hours, holidays)
- Scenario planning

### 5. Risk & Issue Management
- Risk register boards
- Probability/Impact assessment
- Risk heatmap visualization
- Mitigation plan tracking
- Automated escalation

### 6. Automation & Integration
- No-code workflow automation
- Trigger-based actions
- REST API for integrations
- Real-time updates via WebSocket

## Technology Stack

| Component | Technology |
|-----------|------------|
| Backend | Python 3.10+, Flask |
| Database | SQLite (default), PostgreSQL (optional) |
| ORM | SQLAlchemy |
| API | REST + WebSocket |
| Frontend | React 18, TypeScript |
| UI | Tailwind CSS |
| State | Zustand |
| Charts | Recharts |

## Quick Start

### Prerequisites

- Python 3.10 or higher
- Node.js 18 or higher
- npm or yarn

### Backend Setup

```bash
# Navigate to backend directory
cd project-manager/backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
flask init-db

# Run the server
python run.py
```

The backend will start at `http://localhost:5000`

### Frontend Setup

```bash
# Navigate to frontend directory
cd project-manager/frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will start at `http://localhost:3000`

### Default Login

- Email: `admin@projectmanager.local`
- Password: `admin123`

## Project Structure

```
project-manager/
├── backend/
│   ├── app/
│   │   ├── __init__.py          # App factory
│   │   ├── config.py            # Configuration
│   │   ├── models/              # Database models
│   │   ├── api/                 # REST API endpoints
│   │   ├── services/            # Business logic
│   │   └── websocket.py         # Real-time events
│   ├── data/                    # SQLite database
│   ├── uploads/                 # File uploads
│   ├── requirements.txt
│   └── run.py
├── frontend/
│   ├── src/
│   │   ├── components/          # React components
│   │   ├── pages/               # Page components
│   │   ├── stores/              # Zustand stores
│   │   ├── services/            # API services
│   │   └── types/               # TypeScript types
│   ├── package.json
│   └── vite.config.ts
├── ARCHITECTURE.md              # Detailed architecture
└── README.md
```

## API Documentation

### Authentication

```bash
# Login
POST /api/v1/auth/login
Body: { "email": "user@example.com", "password": "password" }

# Register
POST /api/v1/auth/register
Body: { "email": "user@example.com", "password": "password", "name": "User Name" }
```

### Projects

```bash
# List projects
GET /api/v1/projects

# Create project
POST /api/v1/projects
Body: { "name": "Project Name", "description": "..." }

# Get project
GET /api/v1/projects/:id

# Get critical path
GET /api/v1/projects/:id/critical-path

# Create baseline
POST /api/v1/projects/:id/baselines
```

### Tasks

```bash
# List tasks
GET /api/v1/tasks?board_id=1

# Create task
POST /api/v1/tasks
Body: { "board_id": 1, "title": "Task Title" }

# Update task
PUT /api/v1/tasks/:id

# Add dependency
POST /api/v1/tasks/:id/dependencies
Body: { "depends_on_id": 2 }

# Log time
POST /api/v1/tasks/:id/time-entries
Body: { "hours": 2.5, "description": "..." }
```

### Resources

```bash
# Get workload
GET /api/v1/resources/workload

# Get forecast
GET /api/v1/resources/forecast?weeks=8

# Allocate resource
POST /api/v1/resources/allocate
Body: { "task_id": 1, "user_id": 2 }
```

### Risks

```bash
# List risks
GET /api/v1/risks

# Create risk
POST /api/v1/risks
Body: { "project_id": 1, "title": "Risk", "probability": "high", "impact": "medium" }

# Get risk matrix
GET /api/v1/risks/matrix
```

## Configuration

### Environment Variables

```bash
# Backend (.env)
FLASK_ENV=development
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret
DATABASE_URL=sqlite:///data/projectmanager.db

# For production with PostgreSQL:
DATABASE_URL=postgresql://user:password@localhost/projectmanager
```

## Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up -d
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details
