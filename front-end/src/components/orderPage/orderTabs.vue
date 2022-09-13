<template>
    <el-tabs
      v-model="activeName"
      type="card"
      class="demo-tabs"
      @tab-click="handleClick"
    >
      <el-tab-pane label="点餐" name="first">User</el-tab-pane>
      <el-tab-pane label="评价" name="second">Config</el-tab-pane>
      <el-tab-pane label="商家" name="third">Role</el-tab-pane>
    </el-tabs>
  </template>
  <script>
//   import { ref } from 'vue'
//   import type { TabsPaneContext } from 'element-plus'
  
//   const activeName = ref('first')
  
//   const handleClick = (tab: TabsPaneContext, event: Event) => {
//     console.log(tab, event)
//   }
  </script>
  <style>
  .demo-tabs > .el-tabs__content {
    padding: 32px;
    color: #6b778c;
    font-size: 32px;
    font-weight: 600;
  }
  </style>
  