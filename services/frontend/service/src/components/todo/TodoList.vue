<template>
  <div class="list">
    <div class="list-title">
      {{ list.title }}
    </div>
    <TodoItem
      v-for="item in list.items"
      v-bind:key="item.id"
      v-bind:item="item"
    ></TodoItem>
    <div class="add-item">
      + Add item
    </div>
  </div>
</template>


<script>
  import TodoItem from './TodoItem'

  export default {
    name: 'TodoList',
    components: {
      TodoItem
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
      /*
      addNewItemToList: function(text) {
        this.$store.dispatch('addedItemForList', {
          id: this.list.id, text: text
        })
        this.addItem = false
      }
      */
    }
  }
</script>


<style>
  .list {
    background-color: rgb(235, 236, 240);
    border-radius: 3px;
    display: grid;
    grid-auto-rows: max-content;
    grid-gap: 10px;
    height: max-content;
    padding: 10px;
  }

  .list-title {
    font-weight: bold;
  }

  .add-item {
    padding-top: 10px;
    padding-bottom: 5px;
  }
</style>
