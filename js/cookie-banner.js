var cookieBanner = {
  init: function() {
    cookieBanner.bind();

    var cookieExists = cookieBanner.cookieExists();

    if (!cookieExists) {
      cookieBanner.setCookie();
      cookieBanner.showCookieNotice();
    }
  },

  bind: function() {
    $(".close-button").on("click", cookieBanner.hideCookieNotice);
  },

  cookieExists: function() {
    var cookie = localStorage.getItem("returningShorUser");

    if (cookie) {
      return true;
    } else {
      return false;
    }
  },

  setCookie: function() {
    localStorage.setItem("returningShorUser", true);
  },

  showCookieNotice: function() {
    $(".cookie-banner-wrapper").addClass("is-visible");
  },

  hideCookieNotice: function() {
    $(".cookie-banner-wrapper").removeClass("is-visible");
  }
};

$(function() {
  cookieBanner.init();
});
