# It must be here to retrieve this information from the dummy
core_universal_identifier       = 'eceb00bb-056c-4314-96e4-fabf0cff6c57'
core_universal_identifier_human = u'Generic system; not identified'

db_engine          = 'sqlite'
db_host            = u'localhost'
db_port            = None # None for default
db_database        = u'WebLab'
weblab_db_username = u'weblab'
weblab_db_password = u'weblab'

debug_mode   = True



#########################
# General configuration #
#########################

server_hostaddress = u'localhost'
server_admin       = u''

################################
# Admin Notifier configuration #
################################

mail_notification_enabled = False

##########################
# Sessions configuration #
##########################

core_session_type = u'Memory'

# session_sqlalchemy_engine   = u'sqlite'
# session_sqlalchemy_host     = u'localhost'
# session_sqlalchemy_username = u''
# session_sqlalchemy_password = u''

# session_lock_sqlalchemy_engine   = u'sqlite'
# session_lock_sqlalchemy_host     = u'localhost'
# session_lock_sqlalchemy_username = u''
# session_lock_sqlalchemy_password = u''

# session_redis_host = u'localhost'
# session_redis_port = 6379
# core_session_pool_id = 1
# core_alive_users_session_pool_id = 1

##############################
# Core generic configuration #
##############################
core_store_students_programs      = False
core_store_students_programs_path = 'files_stored'
core_experiment_poll_time         = 350 # seconds

core_server_url = u'http://localhost/weblab/'

############################
# Scheduling configuration #
############################

core_coordination_impl = 'redis'

coordinator_redis_db       = None
coordinator_redis_password = None
coordinator_redis_port     = None
coordinator_redis_host     = None

# core_coordinator_db_name      = u'WebLabCoordination'
# core_coordinator_db_engine    = u'sqlite'
# core_coordinator_db_host      = u'localhost'
# core_coordinator_db_username  = u'weblab'
# core_coordinator_db_password  = u'weblab'

core_coordinator_laboratory_servers = {
    'laboratory1:laboratory1@core_host' : {
            'exp1|dummy|Dummy experiments'        : 'dummy1@dummy_queue',
        },

}

core_coordinator_external_servers = {
    'external-robot-movement@Robot experiments'   : [ 'robot_external' ],
}

weblabdeusto_federation_demo = ('EXTERNAL_WEBLAB_DEUSTO', {
                                    'baseurl' : 'https://weblab.deusto.es/weblab/',
                                    'username' : 'weblabfed',
                                    'password' : 'password',
                                    'experiments_map' : {'external-robot-movement@Robot experiments' : 'robot-movement@Robot experiments'}
                            })

core_scheduling_systems = {
        'dummy_queue'            : ('PRIORITY_QUEUE', {}),
        'robot_external'   : weblabdeusto_federation_demo,
    }

