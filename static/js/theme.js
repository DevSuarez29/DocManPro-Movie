document.addEventListener("DOMContentLoaded", function () {
  const bodyElement = document.getElementById("bodyElement");
  const toggleThemeButtons = document.querySelectorAll("button[data-bs-theme-value]");
  const headtop = document.evaluate("//*[@id='headtop']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;


  // Recuperar el tema y el botón activo almacenados en LocalStorage
  let savedData = JSON.parse(localStorage.getItem("themeData")) || {
    theme: "auto",
    btn: "auto"
  };

  // Función para activar el botón correspondiente al tema activo
  function activateButtonForTheme(theme) {
    toggleThemeButtons.forEach(btn => {
      const themeValue = btn.getAttribute("data-bs-theme-value");
      btn.classList.toggle("active", themeValue === theme);
    });
  }

  function setThemeAndSaveData(themeValue) {
    savedData.theme = themeValue;
    savedData.btn = themeValue;

    // Guardar los datos actualizados en LocalStorage
    localStorage.setItem("themeData", JSON.stringify(savedData));

    if (themeValue === "auto") {
      if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
        bodyElement.setAttribute("data-bs-theme", "dark");
        savedData.theme = "dark";
      } else {
        bodyElement.setAttribute("data-bs-theme", "light");
        savedData.theme = "light";
      }
    } else if (themeValue === "dark") {
      bodyElement.setAttribute("data-bs-theme", "dark");
      headtop.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
    } else if (themeValue === "light") {
      bodyElement.setAttribute("data-bs-theme", "light");
      headtop.style.backgroundColor = 'rgba(255, 255, 255, 0.8)';
    }

    // Activar el botón correspondiente al tema seleccionado
    activateButtonForTheme(themeValue);
  }

  // Aplicar el tema almacenado en LocalStorage
  setThemeAndSaveData(savedData.theme);

  toggleThemeButtons.forEach(button => {
    button.addEventListener("click", function () {
      const themeValue = button.getAttribute("data-bs-theme-value");
      setThemeAndSaveData(themeValue);
    });
  });
});
