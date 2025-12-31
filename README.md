Install this MCP server by adding the following JSON code to your JSON config file

```
{
  "mcpServers": {
    "mcp-chess": {
      "command": "/Users/biaohu/.local/bin/uvx",
      "args": [
        "--from",
        "git+https://github.com/ermao1688/mcp-chess.git",
        "chess"
      ]
    }
  }
}
```
