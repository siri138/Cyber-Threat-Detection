from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ThreatDetection
from django.db.models import Count
import ipaddress
@api_view(['POST'])
def detect_threat(request):

    ip_address = request.data.get('ip_address')
    failed_attempts = request.data.get('failed_attempts')

    if not ip_address or failed_attempts is None:
        return Response({
            "error": "IP address and failed attempts are required"
        }, status=400)
    try:
        ipaddress.ip_address(str(ip_address).strip())
    except ValueError:
        return Response({
            "error": "Please enter a valid IP address"
        }, status=400)
    try:
        
        failed_attempts = int(failed_attempts)
    except (ValueError, TypeError):
        return Response({
            "error": "Failed attempts must be a number"
        }, status=400)

    if failed_attempts < 0:
        return Response({
            "error": "Failed attempts cannot be negative"
        }, status=400)

    if failed_attempts >= 5:
        status = "Threat Detected"
        threat = "Possible Brute Force Attack"
        severity = "High"

    elif failed_attempts >= 3:
        status = "Suspicious Activity"
        threat = "Unusual Login Attempts"
        severity = "Medium"

    else:
        status = "Safe"
        threat = "No suspicious activity"
        severity = "Low"

    # Save detection history in database
    ThreatDetection.objects.create(
        ip_address=ip_address,
        failed_attempts=failed_attempts,
        status=status,
        threat=threat,
        severity=severity
    )

    return Response({
        "ip_address": ip_address,
        "status": status,
        "threat": threat,
        "severity": severity
    })

@api_view(['GET'])
def dashboard_stats(request):

    total = ThreatDetection.objects.count()

    threats = ThreatDetection.objects.filter(
        status="Threat Detected"
    ).count()

    safe = ThreatDetection.objects.filter(
        status="Safe"
    ).count()

    high = ThreatDetection.objects.filter(
        severity="High"
    ).count()

    return Response({
        "total_scans": total,
        "total_threats": threats,
        "safe_activities": safe,
        "high_severity": high
    })
@api_view(['GET'])
def threat_history(request):
    records = ThreatDetection.objects.all().order_by('-created_at')

    history = []

    for record in records:
        history.append({
            "ip_address": record.ip_address,
            "failed_attempts": record.failed_attempts,
            "threat": record.threat,
            "severity": record.severity,
            "created_at": record.created_at
        })

    return Response(history)