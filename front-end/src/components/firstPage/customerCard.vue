<template>
    <el-card shadow="hover" class="customerCardClass">
        <el-row class = "customerCardRow">
            <el-col :span="12" class = "customerForm1Col">
                <customer-form-1/>
            </el-col>

            <el-col :span="12" class = "customerForm2Col">
                <customer-form-2/>
            </el-col>
        </el-row>
    </el-card>

</template>

<script>
import customerForm1 from './customerForm1.vue'
import customerForm2 from './customerForm2.vue'

export default {
  name: 'customerCard',
  components: {
    customerForm1,
    customerForm2,
  }
}
</script>

<style>

.customerCardClass {
    width: 660px;
    height: 350px;
}

.customerCardRow {
    margin-top: 0px;
}

.customerForm1Col {
    margin-top: 0px;
}



</style>
