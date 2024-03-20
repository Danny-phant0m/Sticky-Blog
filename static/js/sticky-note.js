class StickyNote extends HTMLElement {
    constructor() {
      super();
      this._data = { header: '', paragraph: '' };
      this.render();
    }
  
    static get observedAttributes() {
      return ['data'];
    }
  
    attributeChangedCallback(name, oldValue, newValue) {
      if (name === 'data' && oldValue !== newValue) {
        this._data = JSON.parse(newValue);
        this.render();
      }
    }
  
    render() {
      this.innerHTML = ''; // Clear previous content
  
      const wrapper = document.createElement('div');
      wrapper.classList.add('sticky-note');
  
      const heading = document.createElement('h2');
      heading.textContent = this._data.header;
      heading.classList.add('h2');
  
      const paragraph = document.createElement('p');
      paragraph.textContent = this._data.paragraph;
      paragraph.classList.add('p');
  
      const editButton = document.createElement('button');
      editButton.textContent = 'edit';
      editButton.classList.add('button');

      const deletebutton = document.createElement('button');
      deletebutton.textContent = 'delete';
      deletebutton.classList.add('second-button');
  
      wrapper.appendChild(heading);
      wrapper.appendChild(paragraph);
      wrapper.appendChild(editButton);
      wrapper.appendChild(deletebutton);
  
      this.appendChild(wrapper);
    }
  }
  
  customElements.define('sticky-note', StickyNote);
  