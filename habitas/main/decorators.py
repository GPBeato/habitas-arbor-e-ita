from functools import wraps
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib import messages


def gestor_required(view_func):
    """Requer que o usuário seja Gestor (Nível 1)"""
    @wraps(view_func)
    @login_required
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_gestor():
            messages.error(request, "Acesso negado. Apenas gestores podem acessar esta página.")
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapped_view


def tecnico_required(view_func):
    """Requer que o usuário seja Técnico aprovado (Nível 2)"""
    @wraps(view_func)
    @login_required
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_tecnico():
            messages.error(request, "Acesso negado. Apenas técnicos aprovados podem acessar esta página.")
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapped_view


def cidadao_required(view_func):
    """Requer que o usuário esteja autenticado (qualquer nível)"""
    @wraps(view_func)
    @login_required
    def wrapped_view(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return wrapped_view


def gestor_ou_tecnico_required(view_func):
    """Requer que o usuário seja Gestor ou Técnico"""
    @wraps(view_func)
    @login_required
    def wrapped_view(request, *args, **kwargs):
        if not (request.user.is_gestor() or request.user.is_tecnico()):
            messages.error(request, "Acesso negado.")
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapped_view
