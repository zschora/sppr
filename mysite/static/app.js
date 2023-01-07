const inputs = document.querySelectorAll('.ratingInput')
function onRatingChange(e) {
    const value = e.target.value
    const label = e.target.labels[0]
    label.innerHTML = `${value}/10`
}

inputs.forEach((input, i) => input.addEventListener('input', onRatingChange))