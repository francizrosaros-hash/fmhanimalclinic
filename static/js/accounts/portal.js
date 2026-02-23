document.addEventListener('DOMContentLoaded', function() {
  // Mobile Sidebar Toggle
  const wrapper = document.getElementById('portalWrapper');
  const toggle = document.getElementById('sidebarToggle');
  const overlay = document.getElementById('mobileOverlay');
  
  if (toggle) {
    toggle.addEventListener('click', () => wrapper.classList.toggle('mobile-open'));
  }
  if (overlay) {
    overlay.addEventListener('click', () => wrapper.classList.remove('mobile-open'));
  }

  // Profile Dropdown Toggle
  const profileBtn = document.getElementById('profileDropdownBtn');
  const profileContainer = profileBtn ? profileBtn.parentElement : null;

  if (profileBtn && profileContainer) {
    profileBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      profileContainer.classList.toggle('active');
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
      if (!profileContainer.contains(e.target)) {
        profileContainer.classList.remove('active');
      }
    });
  }

});
