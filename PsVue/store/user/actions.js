export default {
    getUser(context) {
        return this.$axios.$get("users")
            .then((response) => {
                context.commit('STORE', response);
                return response;
            });
    }
}