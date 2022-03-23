class PrimaryReplicaRouter:

    route_app_labels = {'core', 'djecommerce'}

    def allow_relation(self, obj1, obj2, **hints):
        db_set = {'users', 'default', 'some'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None




