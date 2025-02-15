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
