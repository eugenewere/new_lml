$(function(){
    $(".customer").slice(0, 6).show(); // select the first ten
    $("#load").click(function(e){ // click event for load more
        e.preventDefault();
        $(".customer:hidden").slice(0, 6).show(); // select next 10 hidden divs and show them
        if($(".customer:hidden").length == 0){ // check if any hidden divs still exist
            spinner.hide();
            swal.fire({
                title: "Error!",
                text: "No more categories to load",
                type: "error",
                confirmButtonText: "Retry"
            });
        }
    });
    $('a[href="#top"]').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 600);
        return false;
    });

    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('.totop a').fadeIn();
        } else {
            $('.totop a').fadeOut();
        }
    });

});
$(document).ready(function(){
    $('a[data-toggle="pill"]').on('show.bs.tab', function(e) {

        localStorage.setItem('activeTab2', $(e.target).attr('href'));
    });
    var activeTab = localStorage.getItem('activeTab2');
    if(activeTab){
        $('#simple-design-tab a[href="' + activeTab + '"]').tab('show');
    }
});



const num = 50;
const files = document.querySelector(".filemanager--files").firstElementChild;
const info = document.querySelector(".filemanager--info").firstElementChild;
const tabs = document.querySelector(".filemanager--tabs");
const controls = document.querySelectorAll(".filemanager--controls");
const btns = Array.from(document.querySelectorAll(".toggle"));
const types = [{type: "audio", ext: ".mp3"}, {type: "image", ext: "jpg"}, {type: "archive", ext: "zip"}, {type: "doc", ext: "txt"}];

let currentFilter = "*";

// Init instance
const SELECTABLE = new Selectable({
	appendTo: ".filemanager--files",
	ignore: ".filemanager--remove", // allow remove buttons to work
});

// Listen for init event
SELECTABLE.on("init", update);

// Listen for update event
SELECTABLE.on("update", update);

// Listen for end event
SELECTABLE.on("end", update);

init();

function init() {
	const frag = document.createDocumentFragment();

	for ( let i = 0; i < num; i++ ) {
		frag.appendChild(createFile({
			size: getRandomInt(10, 150),
			name: generateId()
		}));
	}

	files.appendChild(frag);

	files.addEventListener("click", e => {
		if ( e.target.classList.contains("filemanager--remove") ) {
			var confim = confirm("Remove file?");
			if ( confirm )
				remove(e.target.closest(".filemanager--file"), true);
		}
	}, false);

	SELECTABLE.add(".filemanager--file");

	tabs.addEventListener("click", e => {
		var node = e.target;

		if ( node.nodeName === "A" && "filter" in node.dataset ) {

			e.preventDefault();

			Array.from(tabs.getElementsByTagName("li")).forEach(el => el.classList.toggle("active", el === node.parentNode));

			filter(node.dataset.filter);

			// disable selecting if in recycle bin
			if ( node.dataset.filter === "trash" ) {
				SELECTABLE.disable();
			} else {
				SELECTABLE.enable();
			}
		}
	}, false);

	controls[0].addEventListener("click", view);
}

function filter(type) {
	type = type || currentFilter;
	if ( type === "*" ) {
		Array.from(files.children).forEach(node => {
			node.style.display = !node.classList.contains("trash") ? "" : "none";
		});
	} else {
		Array.from(files.children).forEach(node => {
			if ( type === "trash"  ) {
				node.style.display = node.classList.contains("trash") ? "" : "none";
			} else {
				node.style.display = node.classList.contains(type) && !node.classList.contains("trash") ? "" : "none";
			}
		});
	}
	currentFilter = type;
}

function view(e) {

	const node = e.target, data = node.dataset;

	if ( "view" in data ) {
		Array.from(controls[0].children).map(el => el.classList.toggle("active", el === node))

		files.parentNode.classList.toggle("filemanager--list", data.view === "list");
	}
}

function update() {
	const selected = SELECTABLE.getSelectedItems();
	btns.forEach(btn => btn.classList.toggle("hidden", !selected.length));
	document.getElementById("filecount").textContent = `${SELECTABLE.items.length} Files (${selected.length} Selected)`
}

function createFile(o) {
	const type = random(types);
	const li = document.createElement("li");
	const template = `
		<div class="filemanager--fileicon">
			<span class="mdi"></span>
		</div>
        <div class="filemanager--remove">&times;</div>
		<div class="filemanager--fileinfo">
			<div class="filemanager--filename">${o.name}.${type.ext}</div>
			<div class="filemanager--filesize">${o.size} ${type.type === "doc" || type.type === "image" ? "KB" : "MB"}</div>
		</div>
`;

	li.classList.add("filemanager--file", type.type);
	li.innerHTML = template;

	return li;
}

function add() {
	filter("*");

	Array.from(tabs.getElementsByTagName("li")).forEach((el, i) => el.classList.toggle("active", i < 1));

	const newfile = createFile({
			size: getRandomInt(10, 150),
			name: generateId()
		});

	if ( files.childElementCount ) {
		files.insertBefore(newfile, files.firstElementChild);
	} else {
		files.appendChild(newfile);
	}

	SELECTABLE.add(newfile);
}

function remove(file, single) {
	let selected = Array.from(document.getElementsByClassName("ui-selected"));

	const data = [];
	const els = Array.from(files.children);
	let index = 0;

	if ( !file ) {
		if ( selected.length ) {
			file = selected;
		} else {
			file = files.firstElementChild;
		}
	}

	if ( files.childElementCount > 0 ) {
		if ( single ) {
			index = els.indexOf(file);
			SELECTABLE.remove(file);
			file.classList.add("trash");
		} else {
			SELECTABLE.remove(selected);
			if ( Array.isArray(file) ) {
				index = selected.length - 1;
				for ( let i = index; i >= 0; i-- ) {
					selected[i].classList.add("trash");
				}
			} else {
				index = els.indexOf(file);
				file.classList.add("trash");
			}

			btns.forEach(btn => btn.classList.add("hidden"));

			info.innerHTML = "";
		}

		els.forEach((el, i) => {
			// Only animate the tags proceeding the deleted tag
			if ( i >= index ) {
				data.push({
					el: el,
					position: el.getBoundingClientRect()
				});
			}
		});

		filter();

		// Animate the tags affected by the change in the DOM
		// when the tag is removed
		data.forEach(function(obj, i) {
			animate(obj);
		});
	}
}

function invert() {
	if ( files.childElementCount ) {
		SELECTABLE.invert();
		update();
	}
}

function selectAll() {
	if ( files.childElementCount ) {
		SELECTABLE.selectAll();
		update();
	}
}

function clearAll() {
	SELECTABLE.clear();
	update();
	btns.forEach(btn => btn.classList.add("hidden"));
}

function random(arr) {
	return arr[Math.floor(Math.random() * arr.length)];
}

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Random filename generation
function generateId(len) {
	len = len || getRandomInt(6,18) / 2;
  var arr = new Uint8Array(parseInt(len, 10));
  window.crypto.getRandomValues(arr)
  return Array.from(arr, dec2hex).join('')
}

// Random filename generation
function dec2hex (dec) {
  return ('0' + dec.toString(16)).substr(-2)
}

// Animate an element's change in position
// caused by a change in the DOM order
function animate(obj) {
	let css = obj.el.style;

	// Get the node's positon AFTER the change
	let r = obj.el.getBoundingClientRect();

	// Calculate the difference in position
	let x = obj.position.left - r.left;
	let y = obj.position.top - r.top;

	// Move the node to it's original position before the DOM change
	css.transform = `translate3d(${x}px, ${y}px, 0px)`;

	// Trigger a repaint so the next bit works
	obj.el.offsetHeight;

	// Reset the transform, but add a transition so it's smooth
	css.transform = `translate3d(0px, 0px, 0px)`;
	css.transition = `transform 250ms`;

	// Reset the style
	setTimeout(function() {
		css.transform = ``;
		css.transition = ``;
	}, 250);
}