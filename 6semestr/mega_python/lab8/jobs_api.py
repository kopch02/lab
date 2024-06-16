from flask import Blueprint, jsonify, request

from data import db_session
from data.jobs import Jobs
from num1 import add_jobs

blueprint = Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_news():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return jsonify({
        'jobs': [
            item.to_dict(only=('job', 'collaborators', 'user.surname',
                               "user.name")) for item in jobs
        ]
    })


@blueprint.route('/api/jobs/<int:job_id>')
def get_one_job(job_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(job_id)
    if not jobs:
        return jsonify({"error": "Not found"})
    return jsonify({
        "job":
        jobs.to_dict(only=("user.name", "user.surname", "user.id", "job",
                           "work_size", "collaborators", "start_date",
                           "end_date", "is_finished", "categories"))
    })


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'Error': 'Empty Request'})
    elif not all(
            key in request.json
            for key in ['team_leader', 'job', 'work_size', 'collaborators']):
        return jsonify({'Error': 'Bad Request'})
    add_jobs(
        request.json['team_leader'],
        request.json['job'],
        request.json['work_size'],
        request.json['collaborators'],
    )
    return jsonify({'Success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_jobs(jobs_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(jobs_id)
    if not jobs:
        return jsonify({'Error': 'Not Found'})
    session.delete(jobs)
    session.commit()
    return jsonify({'Success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['PUT'])
def modify_jobs(jobs_id):
    if not request.json:
        return jsonify({'Errors': 'Empty Request'})
    elif not all(key in request.json for key in [
            'team_leader', 'job', 'work_size', 'collaborators'
    ]):
        return jsonify({'error':'bad request'})
    session = db_session.create_session()
    jobs = session.query(Jobs).filter(Jobs.id == jobs_id).first()
    if not jobs:
        return jsonify({'Error':'Not Found'})
    jobs.team_leader = request.json['team_leader']
    jobs.job = request.json['job']
    jobs.collaborators = request.json['collaborators']
    jobs.work_size = request.json['work_size']
    session.commit()
    return jsonify({'Success': 'OK'})
    