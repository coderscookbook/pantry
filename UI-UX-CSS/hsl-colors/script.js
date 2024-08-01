document.addEventListener("DOMContentLoaded", function() {
  const colorDiv    = document.querySelector(".color");
  // const rowItemDiv  = document.querySelector(".row-item");

  const hue         = getComputedStyle(colorDiv).getPropertyValue("--hue").trim();
  const saturation  = getComputedStyle(colorDiv).getPropertyValue("--saturation").trim();
  const lightness   = getComputedStyle(colorDiv).getPropertyValue("--lightness").trim();

  
  colorDiv.textContent = `Hue: ${hue}\nSaturation: ${saturation}\nLightness: ${lightness}`;
})

