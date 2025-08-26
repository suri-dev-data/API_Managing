# 🏟️ Match Notifier Bot

This is a Python-based automation tool that checks when two specific football teams are scheduled to play and sends a notification via SMS using Twilio. It uses **web scraping** to gather match information from Google and **Twilio's API** to deliver real-time alerts.

## 📌 Features

- Scrapes Google search results to find upcoming matches between two teams
- Parses and extracts match date and time
- Sends Whatsapp notifications using Twilio
- Can be scheduled to run periodically (e.g., via cron or Task Scheduler)

## 🚀 How It Works

1. The script performs a Google search like:  
2. It scrapes the search results to find the next scheduled game.
3. Once a match is detected, it formats the date/time.
4. A notification is sent via Twilio to your phone number.

## 🛠️ Technologies Used

- `requests` and `GoogleAPI` for web scraping
- `Twilio` for Whatsapp notifications
- `os` and `dotenv` for environment variable management
