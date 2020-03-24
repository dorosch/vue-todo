<template>
  <ul>
    <h4>
      {{ list.title }}
    </h4>
    <TodoItem
      v-for="item in list.items"
      v-bind:key="item.id"
      v-bind:item="item"
    ></TodoItem>
    <div v-if="!addItem">
      <button
        v-on:click="addItem = !addItem"
      >
        +
      </button>
    </div>
    <div v-else>
      <input
        v-focus
        v-model="text"
        v-on:keyup.enter="addNewItemToList"
        @blur="addItem = !addItem; text = ''"
      />
      <button
        v-if="text.length >= 1"
        @mousedown="addNewItemToList"
      >
        Add
      </button>
    </div>
  </ul>
</template>


<script>
  import TodoItem from './TodoItem'

  export default {
    name: 'TodoList',
    components: {
      TodoItem
    },
    props: {
      list: Array
    },
    data: function() {
      return {
        text: '',
        addItem: false
      }
    },
    methods: {
      addNewItemToList: function() {
        this.$store.dispatch('addedItemForList', {
          id: this.list.id, text: this.text
        })
        this.text = ''
        this.addItem = !this.addItem
      }
    },
    directives: {
      focus: {
        inserted: function (el) {
          el.focus()
        }
      }
    }
  }
</script>
