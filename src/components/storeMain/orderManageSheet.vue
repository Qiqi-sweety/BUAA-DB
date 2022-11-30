<template>
    <n-tabs type="segment">
    <n-tab-pane name="未处理" tab="未处理">
        <el-row>
            <el-col :span="6"><orderSheetCard2/></el-col>
            <el-col :span="6"><orderSheetCard2/></el-col>
            <el-col :span="6"><orderSheetCard2/></el-col>
            <el-col :span="6"><orderSheetCard2/></el-col>
        </el-row>
        
      
    </n-tab-pane>
    <n-tab-pane name="已处理" tab="已处理">
        <el-row>
            <el-col :span="6"><orderSheetCard3/></el-col>
            <el-col :span="6"><orderSheetCard3/></el-col>
            <el-col :span="6"><orderSheetCard3/></el-col>
            <el-col :span="6"><orderSheetCard3/></el-col>
        </el-row>
    </n-tab-pane>
  </n-tabs>
    
</template>

<script>
  import { defineComponent ,ref } from 'vue'
  import { NCard,NRate,NTabs,NTabPane} from 'naive-ui'
  import orderSheetCard2 from '../cards/orderSheetCard2.vue'
  import orderSheetCard3 from '../cards/orderSheetCard3.vue'

  export default defineComponent({
    components: {
      NCard,
      NRate,
      NTabPane,
      NTabs,
      orderSheetCard2,
      orderSheetCard3,
    },
    setup() {
      return {
      }
    }
  })
</script>