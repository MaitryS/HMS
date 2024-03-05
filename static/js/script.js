// Add event listener to all alerts with class 'alert-dismissible'
document.querySelectorAll('.alert-dismissible').forEach(alert => {
    alert.addEventListener('closed.bs.alert', () => {
      // Remove the alert after it has been closed
      alert.remove();
    });
  
    // Automatically close alerts after 2 seconds
    setTimeout(() => {
      document.querySelectorAll('.alert').forEach(alert => {
        // Trigger the 'close' event on each alert after 2 seconds
        const bsAlert = new bootstrap.Alert(alert);
        bsAlert.close();
      });
    }, 2000);
  });


  // -----------------login----------------
  
  // -----------------login----------------