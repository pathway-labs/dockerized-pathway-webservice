import os

import pathway as pw

PORT = int(os.getenv("PORT", "8080"))


class InputSchema(pw.Schema):
    input: str


webserver = pw.io.http.PathwayWebserver(
    host="0.0.0.0",
    port=PORT,
)

input, response_writer = pw.io.http.rest_connector(
    webserver=webserver,
    schema=InputSchema,
    delete_completed_queries=True,
)

output = input.select(query_id=input.id, result=pw.this.input.str.upper())

response_writer(output)

pw.run(monitoring_level=pw.MonitoringLevel.NONE)
