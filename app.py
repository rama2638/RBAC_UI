import streamlit as st
import openai 
import os
# Mock Database
users = []
roles = []
openai.api_key = os.getenv("OPENAI_API_KEY")

# OpenAI API Key (Replace with your own key)
openai.api_key = "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"

# Generate Suggestions (Optional: Use GPT for Role Suggestions)
def generate_role_suggestions(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# User Management
def user_management():
    st.header("User Management")
    with st.form("Add User"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        role = st.selectbox("Role",['software devloper',"web developer"])
        status = st.radio("Status", ["Active", "Inactive"])
        if st.form_submit_button("Add User"):
            if role != "No roles available":

                users.append({"name": name, "email": email, "role": role, "status": status})
                st.success("User added successfully!")
            else:
                st.error("please added a role first.")
            
    st.subheader("User List")
    for idx,user in enumerate(users):
        st.write({"name": name, "email": email, "role": role, "status": status})
        col1,col2=st.columns(2)
        if col1.button(f"edit User{idx+1}"):
            with st.form(f"edit User{idx+1}"):
                name = st.text_input("Name")
                email = st.text_input("Email")
                role = st.selectbox("Role",['software devloper',"web developer"])
                status = st.radio("Status", ["Active", "Inactive"])
                if st.form_submit_button("save changes"):
                    user[idx]={"name": name, "email": email, "role": role, "status": status}
                    st.success("user updated successfully")
                    st.experimental_rerun()
        if col2.button(f"delete user{idx+1}"):
            user.pop(idx)
            st.success("user deleted successfully")
            st.experimental_rerun()


    
# Role Management
def role_management():
    st.header("Role Management")
    with st.form("Add Role"):
        role_name = st.text_input("Role Name")
        permissions = st.multiselect("Permissions", ["Read", "Write", "Delete"])
        if st.form_submit_button("Add Role"):
            roles.append({"role_name": role_name, "permissions": permissions})
            st.success("Role added successfully!")
    st.subheader("Role List")
    for idx, role in enumerate(roles):
        st.write({"role_name": role_name, "permissions": permissions})
        if st.button(f"edit role{idx+1}"):
            with st.form(f"edit role{idx+1}"):
                role_name = st.text_input("Role Name")
                permissions = st.multiselect("Permissions", ["Read", "Write", "Delete"])
                
                if st.form_submit_button("save changes"):
                    roles[idx]={"role_name": role_name, "permissions": permissions}
                    st.success("role updated successfully")
                    st.experimental_rerun()
        

# Permission Management
def permission_management():
    st.header("Permission Management")
    st.subheader("Assign or Modify Permissions for Roles")
    
    if not roles:
        st.warning("No roles available. Please add roles first in Role Management.")
        return
    
    # Iterate through each role
    for idx, role in enumerate(roles):
        st.write(f"**Role**: {role['role_name']}")
        current_permissions = role.get("permissions", [])
        
        # Display permissions and allow modifications
        new_permissions = st.multiselect(
            f"Modify Permissions for '{role['role_name']}'", 
            ["Read", "Write", "Delete"], 
            default=current_permissions
        )

        
        # Save changes
        if st.button(f"Save Changes for '{role['role_name']}'"):
            roles[idx]["permissions"] = new_permissions
            st.success(f"Permissions updated for role: {role['role_name']}")
            st.experimental_rerun() 



# API Simulation
def api_simulation():
    st.header("API Simulation")
    st.write("Mock API calls for CRUD operations")

# Main Application
def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose the app mode", ["User Management", "Role Management", "Permission Management", "API Simulation"])
    
    if app_mode == "User Management":
        user_management()
    
    elif app_mode == "Role Management":
        role_management()
    elif app_mode == "Permission Management":
        permission_management()
    elif app_mode == "API Simulation":
        api_simulation()

if __name__ == "__main__":
    main()