<template>
    <el-row class = "orderSheetRowClass">
      <el-col :span="12" v-for="c in info.comments">
        <rateCard1 :comment="c"/>
      </el-col>
    </el-row>
</template>

<script setup>
import {defineProps, reactive, onMounted} from 'vue'
import {show_comments} from "@/api/store";

const info = reactive({
  comments: []
})
const props = defineProps({store_id: String})

onMounted(() => {
  show_comments().then(res => {
    let content = res.data
    console.log(content)
    info.comments = []
    if (content.code === "200") {
      content.comment_list.forEach(item => {
        info.comments.push(item)
      })
    }
  })
})
</script>