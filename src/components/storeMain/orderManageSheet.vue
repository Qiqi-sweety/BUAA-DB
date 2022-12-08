<template>
    <n-tabs type="segment">
    <n-tab-pane name="未处理" tab="未处理">
        <el-row>
          <div v-for="order in info.unhandled_orders">
            <el-col :span="6"><orderSheetCard2 :order="order"/></el-col>
          </div>
        </el-row>
        
      
    </n-tab-pane>
    <n-tab-pane name="已处理" tab="已处理">
        <el-row>
          <div v-for="order in info.handled_orders">
            <el-col :span="6"><orderSheetCard3 :order="order"/></el-col>
          </div>
        </el-row>
    </n-tab-pane>
  </n-tabs>
    
</template>

<script setup>
import {NTabs, NTabPane} from 'naive-ui'
import {show_orders} from "@/api/store";
import {onMounted, reactive} from "vue";

const info = reactive({
  handled_orders: [],
  unhandled_orders: [],
})
onMounted(() => {
  show_orders({
    isProcessed: true
  }).then(res => {
    let content = res.data
    console.log(content)
    if (content.code === "200") {
      content.list.forEach(item => {
        info.handled_orders.push(item)
      })
    }
  })
  show_orders({
    isProcessed: false
  }).then(res => {
    let content = res.data
    console.log(content)
    if (content.code === "200") {
      content.list.forEach(item => {
        info.unhandled_orders.push(item)
      })
    }
  })
})
</script>