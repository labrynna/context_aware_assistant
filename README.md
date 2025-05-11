# 🧠 Context-Aware Conversational Assistant

## Overview
An end-to-end intelligent assistant that automates interaction over a web interface using large language models.  
It can track conversation context, auto-generate meaningful replies, detect action items (like date invitations), and maintain a real-time schedule to avoid conflicts.

This assistant is designed for seamless, human-like interactions across ongoing conversations—ideal for professional follow-ups, social planning, or customer engagement.

## Key Features

- 🤖 **Contextual Chat Management**: Maintains separate memory files for each conversation
- ✍️ **AI-Generated Replies**: Uses Gemini API to craft replies tailored to the other person’s style, background, and ongoing context
- 📅 **Smart Scheduling**: Detects appointments within messages, extracts time/date/location, and prevents double-booking
- 📬 **Email Alerts**: Automatically sends appointment details and conversation summaries to your inbox
- 🔁 **Fully Automated Workflow**: Operates autonomously through scheduled checks, updates, and messaging

## Technologies Used
- Python
- Selenium
- Gemini API
- JSON/Structured Storage
- Email (SMTP)
- Timezone-aware scheduling

## Example Use Case
A user receives dozens of messages across different chats. This assistant:
- Tracks all conversations
- Auto-generates personalized replies using Gemini
- Extracts commitments like “Let’s meet Friday at 8pm at Soho House”
- Sends the details to their inbox
- Ensures no overlapping appointments

## Results
- ⏱ Saved hours of repetitive messaging
- 📅 Avoided double-bookings
- 💬 Maintained high-quality, contextual conversation with 95% accuracy
