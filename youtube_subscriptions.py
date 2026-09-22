from storage.engine import CollectionStore, NOW

CollectionName = 'youtube_subscriptions'
_store = CollectionStore(
    name=CollectionName,
    defaults={'enabled': True, 'last_live_id': None, 'created_at': NOW},
    unique_sets=[['guild_id', 'channel_id']],
    json_fields=set(),
    datetime_fields={'created_at'},
    sequence_fields={},
)

async def create_table():
    return await _store.prepare()

async def insert(id=None, guild_id=None, channel_id=None, channel_title=None, channel_url=None,
                 notify_channel_id=None, role_id=None, enabled=True, last_live_id=None, created_at=None):
    return await _store.insert(locals())

async def update(id, guild_id=None, channel_id=None, channel_title=None, channel_url=None,
                 notify_channel_id=None, role_id=None, enabled=None, last_live_id=None, created_at=None):
    payload = locals()
    if enabled is None:
        payload.pop('enabled', None)
    return await _store.update(payload)

async def get(id=None, guild_id=None, channel_id=None, channel_title=None, channel_url=None,
              notify_channel_id=None, role_id=None, enabled=None, last_live_id=None, created_at=None):
    payload = locals()
    if enabled is None:
        payload.pop('enabled', None)
    return await _store.get(payload)

async def gets(id=None, guild_id=None, channel_id=None, channel_title=None, channel_url=None,
               notify_channel_id=None, role_id=None, enabled=None, last_live_id=None, created_at=None):
    payload = locals()
    if enabled is None:
        payload.pop('enabled', None)
    return await _store.gets(payload)

async def delete(id=None, guild_id=None, channel_id=None, channel_title=None, channel_url=None,
                 notify_channel_id=None, role_id=None, enabled=None, last_live_id=None, created_at=None):
    payload = locals()
    if enabled is None:
        payload.pop('enabled', None)
    return await _store.delete(payload)

async def get_all():
    return await _store.get_all()
