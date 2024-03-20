class StickyNote extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        this._data = { header: '', paragraph: '' };
        this.render();
    }

    // Define a static method to observe attribute changes
    static get observedAttributes() {
        return ['data'];//notified when data changes
    }

    // Called when an observed attribute has been added, removed, updated, or replaced.
    attributeChangedCallback(name, oldValue, newValue) {
        if (name === 'data' && oldValue !== newValue) {
            this._data = JSON.parse(newValue);
            this.render();
        }
    }

    // Render method to update the component when data changes
    render() {
        
        const wrapper = document.createElement('div');
        //wrapper.classList.add('sticky-note');

        const heading = document.createElement('h2');
        heading.textContent = this._data.header;

        const paragraph = document.createElement('p');
        paragraph.textContent = this._data.paragraph;

        wrapper.appendChild(heading);
        wrapper.appendChild(paragraph);

        this.shadowRoot.innerHTML = ''; // Clear previous content
        this.shadowRoot.appendChild(wrapper);
    }
}

// Register the StickyNote component using the tag name <sticky-note>.
customElements.define('sticky-note', StickyNote);