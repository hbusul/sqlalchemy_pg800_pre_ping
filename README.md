This repo is only for demonstration of a bug.

`docker-compose up --build` to up the system.

After 10 seconds, from another terminal, `docker-compose restart database`

You should see either a `BrokenPipeError` or a `struct.error`

```log

myapp_1     | 2021-03-19 14:53:01,575 DEBUG sqlalchemy.pool.impl.QueuePool Connection <pg8000.core.Connection object at 0x7f4f59155bd0> checked out from pool
myapp_1     | 2021-03-19 14:53:01,575 DEBUG sqlalchemy.pool.impl.QueuePool Pool pre-ping on connection <pg8000.core.Connection object at 0x7f4f59155bd0>
myapp_1     | Traceback (most recent call last):
myapp_1     |   File "main.py", line 13, in some_func
myapp_1     |     session.scalar(select([1]))
myapp_1     |   File "/usr/local/lib/python3.7/site-packages/sqlalchemy/orm/session.py", line 1276, in scalar
myapp_1     |     clause, params=params, mapper=mapper, bind=bind, **kw
myapp_1     |   File "/usr/local/lib/python3.7/site-packages/sqlalchemy/orm/session.py", line 1268, in execute
myapp_1     |     return self._connection_for_bind(bind, close_with_result=True).execute(
myapp_1     |   File "/usr/local/lib/python3.7/site-packages/sqlalchemy/orm/session.py", line 1130, in _connection_for_bind
myapp_1     |     engine, execution_options
myapp_1     |   File "/usr/local/lib/python3.7/site-packages/sqlalchemy/orm/session.py", line 431, in _connection_for_bind
myapp_1     |     conn = bind._contextual_connect()
myapp_1     |   File "/usr/local/lib/python3.7/site-packages/sqlalchemy/engine/base.py", line 2226, in _contextual_connect
myapp_1     |     self._wrap_pool_connect(self.pool.connect, None),
myapp_1     |   File "/usr/local/lib/python3.7/site-packages/sqlalchemy/engine/base.py", line 2262, in _wrap_pool_connect
myapp_1     |     return fn()
myapp_1     |   File "/usr/local/lib/python3.7/site-packages/sqlalchemy/pool/base.py", line 363, in connect
myapp_1     |     return _ConnectionFairy._checkout(self)
myapp_1     |   File "/usr/local/lib/python3.7/site-packages/sqlalchemy/pool/base.py", line 791, in _checkout
myapp_1     |     result = pool._dialect.do_ping(fairy.connection)
myapp_1     |   File "/usr/local/lib/python3.7/site-packages/sqlalchemy/engine/default.py", line 517, in do_ping
myapp_1     |     cursor.execute(self._dialect_specific_select_one)
myapp_1     |   File "/usr/local/lib/python3.7/site-packages/pg8000/core.py", line 860, in execute
myapp_1     |     self._c.execute(self, "begin transaction", None)
myapp_1     |   File "/usr/local/lib/python3.7/site-packages/pg8000/core.py", line 1908, in execute
myapp_1     |     self._flush()
myapp_1     |   File "/usr/local/lib/python3.7/socket.py", line 607, in write
myapp_1     |     return self._sock.send(b)
myapp_1     | BrokenPipeError: [Errno 32] Broken pipe
myapp_1     | 2021-03-19 14:53:01,576 DEBUG sqlalchemy.pool.impl.QueuePool Connection <pg8000.core.Connection object at 0x7f4f59155bd0> being returned to pool
myapp_1     | 2021-03-19 14:53:01,576 DEBUG sqlalchemy.pool.impl.QueuePool Connection <pg8000.core.Connection object at 0x7f4f59155bd0> rollback-on-return

```

The issue here is that `BrokenPipeError` or `struct.error` does not invalidate the connection.
