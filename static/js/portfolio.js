document.addEventListener("DOMContentLoaded", function() {
    const nameSearch = document.getElementById("name-search")
    const tags = document.querySelectorAll(".tag")
	const categories = document.querySelectorAll(".category")
    const projects = document.querySelectorAll(".project")

    function filterProjects() {
        const nameQuery = nameSearch.value.toLowerCase();
        projects.forEach((project) => {
            const name = project.getAttribute("data-name")
            const nameMath = name.includes(nameQuery)

            if (nameMath) {
                project.style.display = "";
            } else {
                project.style.display = "none";
            }
        })
    }
    tags.forEach((tag) => {
        tag.addEventListener("click", function () {
            const selectedTag = this.getAttribute("data-tag")

            projects.forEach((project) => {
                const projectTags = project.getAttribute("data-tags")
                if (projectTags.includes(selectedTag)) {
                    project.style.display = ""
                } else {
                    project.style.display = "none"
                }
            })
        })
    })
    nameSearch.addEventListener("keyup", filterProjects)
})