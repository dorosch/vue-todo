<template>
  <div class="list">
    <div class="list-title">
      {{ list.title }}
    </div>
    <draggable v-model="list.items" v-bind="dragOptions">
      <transition-group type="transition" name="flip-item">
      <TodoItem
        v-for="item in list.items"
        v-bind:key="item.id"
        v-bind:item="item"
      ></TodoItem>
      </transition-group>
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
    data: function() {
      return {
        addItem: false
      }
    },
    computed: {
      dragOptions: function() {
        return {
          animation: 0,
          group: "description",
          disabled: false,
          ghostClass: "ghost"
        }
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

  .flip-item-move {
    transition: transform 0.5s;
  }

  .no-move {
    transition: transform 0s;
  }
</style>
