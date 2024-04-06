# Hackers Break Into AI Hiring Chatbot, Could Hire and Reject Fast Food Applicants

![rw-book-cover](https://www.404media.co/content/images/size/w1200/2024/01/chattr-header-1.png)

## Metadata
- Author: [[Joseph Cox · Jan 11]]
- Date: 2024-01-11
- Full Title: Hackers Break Into AI Hiring Chatbot, Could Hire and Reject Fast Food Applicants
- Category: #articles
- Summary: Hackers were able to breach the backend of an AI chatbot used by fast food franchises for hiring, potentially allowing them to accept or reject job applicants and access sensitive data. The hackers gained access by exploiting an exposed Firebase configuration related to a fast food chain. They were able to obtain names, phone numbers, email addresses, and other information from the database. The vulnerability was reported to the AI company, Chattr, which fixed the issue, but there was no further contact or thanks from the company.
- URL: https://www.404media.co/hackers-break-into-hiring-ai-chat-bot-chattr/

## Highlights
- A group of hackers gained access to the backend of an AI chatbot that fast food franchises use to help automate hiring. ([View Highlight](https://read.readwise.io/read/01hkxjsqn9zhn2z29ferg6z8qp))
- had access to a wealth of sensitive information on applicants, the fast food franchises, and the AI company itself, called Chattr. ([View Highlight](https://read.readwise.io/read/01hkxjsz5368eaa7fspke8036e))
- Chattr [advertises](https://chattr.ai/?ref=404media.co) itself as “the first ever automated end-to-end hiring software for the hourly workforce powered by an AI digital assistant.” ([View Highlight](https://read.readwise.io/read/01hkxjtnzchhn00t0rnx3nhpk2))
- The script returned a Firebase configuration for what appeared to relate to fast food chain KFC. The researchers took that configuration and put it into Firepwn, [a tool available on Github](https://github.com/0xbigshaq/firepwn-tool?ref=404media.co) used for testing the security of apps using Firebase. At first, the researchers didn’t have the ability to read any of the data stored. But after creating a new user account through Firebase, they gained read and write access to the underlying database. ([View Highlight](https://read.readwise.io/read/01hkxjvvzxr1nscjzjmhn71t1p))
- In their blog post, MrBruh posted multiple screenshots which appear to show conversations between job applicants and Chattr’s bot; upcoming interview dates, and a column marked as “make a decision” with the names of apparent applicants and a thumbs up, thumbs down interface. ([View Highlight](https://read.readwise.io/read/01hkxjxv2e9q89pt87z168cy03))
