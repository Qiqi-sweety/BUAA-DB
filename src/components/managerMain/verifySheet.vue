<!-- manageMainPage的子组件：展示待审核店铺卡片的组件 -->

<!-- TODO:
获取待审核店铺的信息list，并且实例化verifyCard，并展示 -->

<template>
    <el-row>
        <el-col :span="12" v-for="store in info.invalid_stores">
          <verifyCard :store="store"/>
        </el-col>
    </el-row>
    
</template>

<script setup>
import {onMounted, reactive} from "vue";
import {show_info} from "@/api/admin";

const info = reactive({
  invalid_stores: []
})
onMounted(() => {
  show_info({
    kind: "店铺",
    isChecked: false
  }).then(res => {
    let content = res.data
    console.log(content)
    info.invalid_stores = []
    if (content.code === "200") {
      content.list.forEach(item => {
        info.invalid_stores.push(item)
      })
    }
  })
})
</script>