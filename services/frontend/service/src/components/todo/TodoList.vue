<template>
  <div class="list">
    <div class="list-title">
      {{ list.title }}
    </div>
    <draggable
      class="drag-area"
      v-model="list.items"
      @change="change"
      group="id"
      draggable=".item"
    >
      <TodoItem
        class="item"
        v-for="item in list.items"
        v-bind:key="item.id"
        v-bind:item="item"
      ></TodoItem> 
    </draggable>
    <div class="add-item">
      + Add item
    </div>
  </div>
</template>


<script>
  import draggable from 'vuedraggable'

  import TodoItem from './TodoItem'

  export default {
    name: 'TodoList',
    components: {
      draggable,
      TodoItem
    },
    props: {
      list: Object
    },
    methods: {
      change: function({added, removed, moved}) {
        if (added) {
          this.$store.dispatch('addedItemForList', {
            id: this.list.id, text: added.element.text
          })
        }
        else if (removed) {
          this.$store.dispatch('deleteItemById', {
            id: removed.element.id
          })
        }
        else if (moved) {
          console.log(moved)
        }
      }
    }
  }
</script>


<style>
  .list {
    background-color: rgb(235, 236, 240);
    border-radius: 3px;
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

  .drag-area {
    min-height: 30px;
  }
</style>
