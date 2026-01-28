from k6_server import mcp

def main():
    """Main entry point for the k6 MCP server"""
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()