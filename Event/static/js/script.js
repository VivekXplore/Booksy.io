// Add JavaScript for modal handling and form submission
const modal = document.getElementById('auth-modal');
const span = document.getElementsByClassName("close")[0];

// Show login modal when auth buttons are clicked
document.querySelectorAll('.auth-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        modal.style.display = "block";
    });
});

span.onclick = () => modal.style.display = "none";
window.onclick = (event) => {
    if (event.target == modal) modal.style.display = "none";
}

// Booking Form Submission
document.getElementById('pe-booking-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const eventName = document.getElementById('pe-event-name').value;
    const eventDate = document.getElementById('pe-event-date').value;
    const eventTime = document.getElementById('pe-event-time').value;
    const guestCount = document.getElementById('pe-guest-count').value;
    const eventType = document.getElementById('pe-event-type').value;
  
    if (eventName && eventDate && eventTime && guestCount && eventType) {
      alert(`Booking Confirmed!\nEvent: ${eventName}\nDate: ${eventDate}\nTime: ${eventTime}\nGuests: ${guestCount}\nType: ${eventType}`);
      // Here you can add AJAX code to send data to your server.
      this.reset();
    } else {
      alert('Please complete all booking fields.');
    }
  });
  
  // Scheduling Form Submission
  document.getElementById('pe-scheduling-form').addEventListener('submit', function(e) {
    e.preventDefault();
  
    const consultDate = document.getElementById('pe-consult-date').value;
    const consultTime = document.getElementById('pe-consult-time').value;
  
    if (consultDate && consultTime) {
      alert(`Consultation Scheduled on ${consultDate} at ${consultTime}`);
      // Add AJAX or calendar integration here if needed.
      this.reset();
    } else {
      alert('Please select both a date and time for your consultation.');
    }
  });
  
  function openModal(eventType) {
    document.getElementById(eventType + 'Modal').style.display = 'block';
}
function closeModal() {
    document.querySelectorAll('.modal').forEach(modal => {
        modal.style.display = 'none';
    });
}
const chatbotButton = document.getElementById('chatbot-button');
const chatbox = document.getElementById('chatbox');
const sendButton = document.getElementById('send-button');
const inputBox = document.getElementById('input-box');
const chatLog = document.getElementById('chat-log');

chatbotButton.addEventListener('click', () => {
  chatbox.style.display = chatbox.style.display === 'none' ? 'flex' : 'none';
});

sendButton.addEventListener('click', sendMessage);
inputBox.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') sendMessage();
});

function sendMessage() {
  const message = inputBox.value.trim();
  if (!message) return;

  appendMessage('user', message);
  inputBox.value = '';

  fetch('/chat/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    },
    body: JSON.stringify({ message: message })
  })
  .then(response => response.json())
  .then(data => appendMessage('bot', data.response));
}

function appendMessage(sender, message) {
  const div = document.createElement('div');
  div.className = `message ${sender}`;
  div.textContent = (sender === 'user' ? ">> " : "SYS: ") + message;
  chatLog.appendChild(div);
  chatLog.scrollTop = chatLog.scrollHeight;
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}