<!-- personalCenter的子组件：用于展示用户的评价 -->

<!-- TODO：根据该用户的评价list，实例化rateCard2的list，并展示 -->

<template>
    <el-row class = "orderSheetRowClass">
      <el-col :span="12" v-for="c in info.comments">
        <rateCard2 :comment="c"/>
      </el-col>

    </el-row>
</template>

<script setup>
import {onMounted, reactive} from "vue";
import {show_comments} from "@/api/user";
import {ElMessage} from "element-plus";

const info = reactive({
  comments: []
})

onMounted(() => {
  show_comments().then(res => {
    let content = res.data
    console.log(content)
    if (content.code === "200") {
      content.list.forEach(item => {
        info.comments.push(item)
      })
    } else {
      ElMessage({message: content.message, type: "error"})
    }
  })
})

</script>