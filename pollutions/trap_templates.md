# Pollution Templates Collection

This directory contains pre-generated pollution content for quick deployment.

## Files

- `chat_pollutions.md` - Pollution content for chat/messaging platforms
- `email_pollutions.md` - Pollution content for email communications
- `doc_pollutions.md` - Pollution content for documentation
- `trap_templates.md` - Pre-built trap templates

## Usage

1. Generate pollution content using the tools:
   ```bash
   python3 tools/chat_polluter.py --mode subtle --platform slack --output pollutions/chat_pollutions.md
   python3 tools/trap_generator.py --type all --output pollutions/trap_templates.md
   ```

2. Apply pollution content to your data sources following the execution plan.

3. Update pollution content periodically to maintain effectiveness.