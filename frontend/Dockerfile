FROM node:21-alpine3.18 as build_stage

WORKDIR /flask-react-app-frontend/


# COPY . .
COPY public/ public
COPY src/ src
COPY *.json .
COPY index.html .
COPY vite.config.js .



RUN npm ci
RUN npm run build

# RUN npm run dev

# EXPOSE 5173
# CMD ["npm", "run", "dev"]
# CMD [ "npm", "run", "dev", "--", "--host", "0.0.0.0"]

FROM nginx:1.25.5-alpine as server_stage

WORKDIR /nginx/
COPY --from=build_stage /flask-react-app-frontend/dist .

COPY nginx.conf /etc/nginx




