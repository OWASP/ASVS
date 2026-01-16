"""
WebSocket Events for Real-time Collaboration
"""
from flask_socketio import emit, join_room, leave_room
from flask_jwt_extended import decode_token


def register_socket_events(socketio):
    """Register WebSocket event handlers"""

    @socketio.on('connect')
    def handle_connect():
        """Handle client connection"""
        emit('connected', {'status': 'connected'})

    @socketio.on('disconnect')
    def handle_disconnect():
        """Handle client disconnection"""
        pass

    @socketio.on('authenticate')
    def handle_authenticate(data):
        """Authenticate user and join user-specific room"""
        token = data.get('token')
        if token:
            try:
                decoded = decode_token(token)
                user_id = decoded['sub']
                join_room(f'user_{user_id}')
                emit('authenticated', {'user_id': user_id})
            except Exception as e:
                emit('error', {'message': 'Authentication failed'})

    @socketio.on('join_project')
    def handle_join_project(data):
        """Join a project room for real-time updates"""
        project_id = data.get('project_id')
        if project_id:
            join_room(f'project_{project_id}')
            emit('joined_project', {'project_id': project_id})

    @socketio.on('leave_project')
    def handle_leave_project(data):
        """Leave a project room"""
        project_id = data.get('project_id')
        if project_id:
            leave_room(f'project_{project_id}')

    @socketio.on('join_board')
    def handle_join_board(data):
        """Join a board room for real-time task updates"""
        board_id = data.get('board_id')
        if board_id:
            join_room(f'board_{board_id}')
            emit('joined_board', {'board_id': board_id})

    @socketio.on('leave_board')
    def handle_leave_board(data):
        """Leave a board room"""
        board_id = data.get('board_id')
        if board_id:
            leave_room(f'board_{board_id}')

    @socketio.on('task_update')
    def handle_task_update(data):
        """Broadcast task update to board room"""
        board_id = data.get('board_id')
        if board_id:
            emit('task_updated', data, room=f'board_{board_id}', include_self=False)

    @socketio.on('task_move')
    def handle_task_move(data):
        """Broadcast task move (drag-drop) to board room"""
        board_id = data.get('board_id')
        if board_id:
            emit('task_moved', data, room=f'board_{board_id}', include_self=False)

    @socketio.on('comment_added')
    def handle_comment_added(data):
        """Broadcast new comment"""
        task_id = data.get('task_id')
        board_id = data.get('board_id')
        if board_id:
            emit('new_comment', data, room=f'board_{board_id}', include_self=False)

    @socketio.on('typing')
    def handle_typing(data):
        """Broadcast typing indicator"""
        board_id = data.get('board_id')
        if board_id:
            emit('user_typing', {
                'user_id': data.get('user_id'),
                'user_name': data.get('user_name'),
                'task_id': data.get('task_id')
            }, room=f'board_{board_id}', include_self=False)

    @socketio.on('cursor_position')
    def handle_cursor_position(data):
        """Broadcast cursor position for collaborative editing"""
        board_id = data.get('board_id')
        if board_id:
            emit('cursor_update', data, room=f'board_{board_id}', include_self=False)


# Helper functions to emit events from other parts of the application
def emit_task_created(board_id, task_data):
    """Emit task created event"""
    from app import socketio
    socketio.emit('task_created', task_data, room=f'board_{board_id}')


def emit_task_updated(board_id, task_data):
    """Emit task updated event"""
    from app import socketio
    socketio.emit('task_updated', task_data, room=f'board_{board_id}')


def emit_task_deleted(board_id, task_id):
    """Emit task deleted event"""
    from app import socketio
    socketio.emit('task_deleted', {'task_id': task_id}, room=f'board_{board_id}')


def emit_notification(user_id, notification_data):
    """Emit notification to specific user"""
    from app import socketio
    socketio.emit('notification', notification_data, room=f'user_{user_id}')


def emit_project_update(project_id, update_data):
    """Emit project update to all users viewing the project"""
    from app import socketio
    socketio.emit('project_update', update_data, room=f'project_{project_id}')
