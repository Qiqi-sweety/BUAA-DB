<template>
    <el-card shadow="hover" class="userCardClass">
        <el-row class = "userCardRow">
            <el-col :span="12" class = "userForm1Col">
                <user-form-1/>
            </el-col>

            <el-col :span="12" class = "userForm2Col">
                <user-form-2/>
            </el-col>
        </el-row>
    </el-card>

</template>

<script>
import userForm1 from './userForm1.vue'
import userForm2 from './userForm2.vue'

export default {
  name: 'userCard',
  components: {
    userForm1,
    userForm2,
  }
}
</script>

<style>

.userCardClass {
    width: 660px;
    height: 350px;
}

.userCardRow {
    margin-top: 0px;
}

.userForm1Col {
    margin-top: 0px;
}



</style>
