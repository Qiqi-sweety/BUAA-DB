<template>
    <el-row class = "orderSheetRowClass">
        <el-col :span="12"><rateCard1/></el-col>
        <el-col :span="12"><rateCard1/></el-col>
    </el-row>
    <el-row class = "orderSheetRowClass">
        <el-col :span="12"><rateCard1/></el-col>
        <el-col :span="12"><rateCard1/></el-col>
    </el-row>
</template>

<script>
  import { defineComponent ,ref } from 'vue'
  import { NTag,NButton} from 'naive-ui'
  import rateCard1 from '../cards/rateCard1.vue'

  export default defineComponent({
    components: {
      NTag,
      NButton,
      rateCard1,
    },
  })

</script>