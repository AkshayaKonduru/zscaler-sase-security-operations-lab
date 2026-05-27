# Splunk Detection Queries

## View All Logs

```spl
index=zscaler
```

---

## Phishing Attempts by User

```spl
index=zscaler threat_type=phishing
| stats count by user
| sort -count
```

---

## Blocked Traffic by Category

```spl
index=zscaler action=blocked
| stats count by category
| sort -count
```

---

## Top Accessed Domains

```spl
index=zscaler
| stats count by url
| sort -count
```

---

## Users with Most Blocked Activity

```spl
index=zscaler action=blocked
| stats count by user
| sort -count
```

---

## Suspicious Domains

```spl
index=zscaler category=unknown OR threat_type=suspicious
| stats count by url, user, source_ip
| sort -count
```

---

## Malware Activity

```spl
index=zscaler threat_type=malware
| table timestamp user source_ip url action threat_type category
```
