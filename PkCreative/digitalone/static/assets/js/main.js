if ($(document).ready(function() {
    if ($("#nav-elements").length) {
      var e = $("#nav-elements");
      url = window.location.href.split("/"), link = url[url.length - 1], hrefs = e.children("li").children("a"), hrefs.each(function() {
        var e = $(this);
        for (href = e.attr("href"); href === link;) {
          e.addClass("color-primary fw-600");
          break
        }
      })
    }
  }), $(document).ready(function() {
    var e = !!document.documentMode,
      t = !e && !!window.StyleMedia;
    e && $("html").addClass("ie"), t && $("html").addClass("edge")
  }), navigator.userAgent.match(/IEMobile\/10\.0/)) {
  var msViewportStyle = document.createElement("style");
  msViewportStyle.appendChild(document.createTextNode("@-ms-viewport{width:auto!important}")), document.head.appendChild(msViewportStyle)
}