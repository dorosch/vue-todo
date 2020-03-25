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
    <InlineInput
      v-if="addItem"
      @blur="addItem = !addItem"
      v-bind:callback="addNewItemToList"
      v-bind:buttonText="`Add`"
    >
    </InlineInput>
    <button
      v-else
      v-on:click="addItem = !addItem"
    >
      +
    </button>
  </ul>
</template>


<script>
  import TodoItem from './TodoItem'
  import InlineInput from '../input/Inline'

  export default {
    name: 'TodoList',
    components: {
      TodoItem,
      InlineInput
    },
    props: {
      list: Object
    },
    data: function() {
      return {
        addItem: false
      }
    },
    methods: {
      addNewItemToList: function(text) {
        this.$store.dispatch('addedItemForList', {
          id: this.list.id, text: text
        })
        this.addItem = false
      }
    }
  }
</script>
