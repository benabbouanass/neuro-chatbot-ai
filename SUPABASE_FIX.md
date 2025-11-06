# 🔧 Fix Supabase Connection

## Problème
```
could not translate host name "db.xxxxx.supabase.co" to address
```

## ✅ Solution

Dans Streamlit Cloud Secrets, remplacez :

```toml
# ❌ INCORRECT
DB_HOST = "db.xxxxx.supabase.co"

# ✅ CORRECT  
DB_HOST = "aws-0-eu-central-1.pooler.supabase.com"
```

## 📍 Comment trouver la bonne URL

1. **Supabase Dashboard** → Votre projet
2. **Settings** → **Database** 
3. **Connection string** → **URI**
4. Copiez l'host entre `postgresql://` et `:5432`

## 🚀 Configuration pour votre projet

```toml
DB_HOST = "db.vhnujinxfqlnrclxckud.supabase.co"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "@@@Yasmina12345@"
DB_PORT = "5432"
```

Après modification → **Restart app** sur Streamlit Cloud